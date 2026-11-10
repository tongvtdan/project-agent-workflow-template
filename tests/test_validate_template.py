from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validate_template


class TemplateValidationTests(unittest.TestCase):
    def setUp(self):
        self.scratch = tempfile.TemporaryDirectory(prefix="template-validation-")
        self.addCleanup(self.scratch.cleanup)
        self.root = Path(self.scratch.name) / "repo"
        shutil.copytree(
            validate_template.ROOT, self.root,
            ignore=shutil.ignore_patterns(".git", "__pycache__"),
        )
        self.bundle = self.root / "docs/specs/trail-log-offline-save"
        self.tasks = self.bundle / "tasks.md"

    def check(self, expected=None):
        out, err = StringIO(), StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            result = validate_template.validate(self.root)
        if expected is None:
            self.assertEqual(result, 0, err.getvalue())
            self.assertIn("PASS:", out.getvalue())
        else:
            self.assertEqual(result, 1, out.getvalue())
            self.assertIn(expected, err.getvalue())

    def replace(self, path, old, new, count=-1):
        text = path.read_text()
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, count))

    def append(self, path, text):
        with path.open("a") as handle:
            handle.write(text)

    def evidence(self, task="T1", result="PASS", candidate="fixture-version"):
        self.append(
            self.bundle / "activity.md",
            f"\n## E1\n\n- Task: {task}\n"
            "- Timestamp: 2030-04-12T10:00:00Z\n"
            f"- Candidate: {candidate}\n"
            "- Environment: synthetic validator fixture\n"
            "- Procedure: fixture-only recorded check\n"
            f"- Result: {result}\n"
            "- Observation: synthetic exit 0; not an application result\n",
        )

    def pass_task(self, task="T1"):
        text = self.tasks.read_text()
        start = text.index(f"## {task}\n")
        end = text.find("\n## ", start + 1)
        end = len(text) if end == -1 else end
        block = text[start:end].replace("- Verification state: PENDING", "- Verification state: PASS")
        block = block.replace("- Evidence: PENDING", "- Evidence: [E1](activity.md#e1)")
        self.tasks.write_text(text[:start] + block + text[end:])

    def test_template_and_intentional_placeholders_pass(self):
        self.check()

    def test_missing_required_readme_has_useful_error(self):
        (self.root / "README.md").unlink()
        self.check("missing required path: README.md")

    def test_broken_file_link(self):
        self.append(self.root / "README.md", "\n[Broken](missing.md)\n")
        self.check("missing local link target")

    def test_missing_heading_anchor(self):
        self.append(self.root / "README.md", "\n[Broken](AGENTS.md#missing)\n")
        self.check("missing heading anchor")

    def test_hidden_placeholder(self):
        self.append(self.root / "README.md", "\nHidden: <Unfilled Field>\n")
        self.check("wrap prose placeholders")

    def test_ci_starter_mismatch(self):
        self.replace(self.root / ".github/workflows/ci.yml.example", "lint-test-build:", "wrong-job:")
        self.check("expected lint-test-build job")

    def test_link_outside_repo(self):
        self.append(self.root / "README.md", "\n[Outside](../outside.md)\n")
        self.check("local link leaves the repository")

    def test_missing_bundle_file(self):
        (self.bundle / "design.md").unlink()
        self.check("missing bundle file design.md")

    def test_two_requirement_sources_are_rejected(self):
        shutil.copyfile(self.bundle / "requirements.md", self.bundle / "bugfix.md")
        self.check("expected exactly one requirements.md or bugfix.md")

    def test_bugfix_bundle_uses_same_traceability_contract(self):
        target = self.root / "docs/specs/bugfix-example"
        shutil.copytree(self.bundle, target)
        (target / "requirements.md").rename(target / "bugfix.md")
        for path in target.glob("*.md"):
            path.write_text(path.read_text().replace("requirements.md#", "bugfix.md#"))
        self.check()

    def test_unknown_requirement_label_is_rejected(self):
        self.replace(self.tasks, "[R1](requirements.md#r1)", "[R99](requirements.md#r1)", 1)
        self.check("invalid requirement reference R99")

    def test_cross_bundle_requirement_is_rejected(self):
        self.replace(
            self.tasks, "[R1](requirements.md#r1)",
            "[R1](../trail-log-offline-save/requirements.md#r1)", 1,
        )
        self.check("invalid requirement reference R1")

    def test_duplicate_requirement_id(self):
        self.append(self.bundle / "requirements.md", "\n## R1\n\nDuplicate behavior.\n")
        self.check("duplicate R1")

    def test_invalid_requirement_id(self):
        self.append(self.bundle / "requirements.md", "\n## R0\n\nInvalid ID.\n")
        self.check("invalid R-numbered heading")

    def test_requirement_needs_acceptance(self):
        source = self.bundle / "requirements.md"
        line = next(line for line in source.read_text().splitlines() if line.startswith("Acceptance:"))
        self.replace(source, line, "", 1)
        self.check("R1: expected one nonempty Acceptance paragraph")

    def test_duplicate_requirement_behavior(self):
        self.replace(self.bundle / "requirements.md", "## R1\n", "## R1\n\nBehavior: Duplicate.\n", 1)
        self.check("R1: expected one nonempty Behavior paragraph")

    def test_requirement_without_design_or_task_coverage(self):
        self.append(self.bundle / "requirements.md", "\n## R5\n\nUnmapped behavior and acceptance.\n")
        self.check("requirement R5 has no design link")
        self.check("requirement R5 has no task coverage")

    def test_task_requires_linked_requirements(self):
        line = next(line for line in self.tasks.read_text().splitlines() if line.startswith("- Requirements:"))
        self.replace(self.tasks, line, "- Requirements: R1", 1)
        self.check("T1: no valid requirement links")

    def test_duplicate_task_id(self):
        text = self.tasks.read_text()
        block = text[text.index("## T1\n"):text.index("## T2\n")]
        self.append(self.tasks, "\n" + block)
        self.check("duplicate T1")

    def test_unknown_dependency(self):
        self.replace(self.tasks, "- Depends on: none", "- Depends on: T99", 1)
        self.check("unknown dependency 'T99'")

    def test_dependency_cycle(self):
        self.replace(self.tasks, "- Depends on: none", "- Depends on: T4", 1)
        self.check("dependency cycle")

    def test_missing_task_field(self):
        self.replace(self.tasks, "- Owner: implementation writer\n", "", 1)
        self.check("expected one nonempty Owner field")

    def test_pass_requires_evidence(self):
        self.replace(self.tasks, "- Verification state: PENDING", "- Verification state: PASS", 1)
        self.check("PASS requires linked evidence")

    def test_pass_rejects_wrong_task_evidence(self):
        self.pass_task()
        self.evidence(task="T2")
        self.check("evidence e1 missing or belongs to another task")

    def test_pass_rejects_failed_evidence(self):
        self.pass_task()
        self.evidence(result="FAIL")
        self.check("PASS evidence result is not PASS")

    def test_pass_rejects_unresolved_candidate(self):
        self.pass_task()
        self.evidence(candidate="PENDING")
        self.check("PASS evidence has unresolved Candidate")

    def test_pass_rejects_unknown_pending_candidate(self):
        self.pass_task()
        self.evidence(candidate="UNKNOWN/PENDING")
        self.check("PASS evidence has unresolved Candidate")

    def test_pass_requires_verified_dependencies(self):
        self.pass_task("T2")
        self.evidence(task="T2")
        self.check("PASS has unverified dependency T1")

    def test_pass_with_matching_complete_evidence_is_structurally_valid(self):
        self.pass_task()
        self.evidence()
        self.check()


if __name__ == "__main__":
    unittest.main()
