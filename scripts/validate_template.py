#!/usr/bin/env python3
"""Validate this template repository without installing packages."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "AGENTS.md", "CODEX.md", "CLAUDE.md", "CHAT_NAMING.md", "PROJECT_STATE.md",
    "SHORTCUTS.md", "SPEC.md", "DESIGN.md", "WORKFLOW.md", "README.md",
    "app/AGENTS.md", "docs/delivery/reusable-requests.md",
    "docs/delivery/development-team.md", "examples/trail-log.md",
    "karpathy-guidelines/SKILL.md", "karpathy-guidelines/references/examples.md",
    ".github/PULL_REQUEST_TEMPLATE.md", ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/feature_request.md", ".github/workflows/ci.yml.example",
    ".github/workflows/validate-template.yml", "scripts/validate_template.py",
    "docs/specs/README.md", "docs/automation.md",
    "docs/specs/trail-log-offline-save/requirements.md",
    "docs/specs/trail-log-offline-save/design.md",
    "docs/specs/trail-log-offline-save/tasks.md",
    "docs/specs/trail-log-offline-save/activity.md",
    "tests/test_validate_template.py",
)
LINK = re.compile(r"!?\[[^\]]*\]\((<[^>]+>|[^\s)]+)(?:\s+[\"'][^\n]*?[\"'])?\)")
PLACEHOLDER = re.compile(r"<[^<>\n]+>")
REQUIREMENT_LINK = re.compile(r"\[(R[1-9]\d*)\]\(([^)]+)\)")
EVIDENCE_LINK = re.compile(r"\[(?:[^\]]+)\]\(activity\.md#(e[1-9]\d*)\)")
TASK_FIELDS = (
    "Outcome", "Requirements", "Depends on", "Owner", "Scope", "Acceptance",
    "Check", "Verification state", "Evidence", "Issue",
)
EVIDENCE_FIELDS = ("Task", "Timestamp", "Candidate", "Environment", "Procedure", "Result", "Observation")


def without_inline_code(text):
    parts = re.split(r"(\n[ \t]*\n)", text)
    for part_index in range(0, len(parts), 2):
        part = parts[part_index]
        runs = list(re.finditer(r"`+", part))
        masked = list(part)
        index = 0
        while index < len(runs):
            opening = runs[index]
            prefix = part[:opening.start()]
            backslashes = len(prefix) - len(prefix.rstrip(chr(92)))
            if backslashes % 2:
                index += 1
                continue
            closing = next((j for j in range(index + 1, len(runs))
                            if runs[j].group() == opening.group()), None)
            if closing is None:
                index += 1
                continue
            # Backslashes are literal inside code; only the opener can be escaped.
            for position in range(opening.start(), runs[closing].end()):
                if masked[position] != "\n":
                    masked[position] = " "
            index = closing + 1
        parts[part_index] = "".join(masked)
    return "".join(parts)


def link_values(pattern, text, allow_images=False):
    text = without_inline_code(text)
    for match in pattern.finditer(text):
        before = text[match.start() - 1] if match.start() else ""
        if before == chr(92) or (before == "!" and not allow_images):
            continue
        yield match.groups()


def prose(text):
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    lines = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return "\n".join(lines), fence


def slug(heading):
    return re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")


def anchors(text):
    body, _ = prose(text)
    seen = {}
    result = set()
    for heading in re.findall(r"^#{1,6}\s+(.+?)(?:\s+#+)?$", body, re.M):
        base = slug(heading)
        count = seen.get(base, 0)
        result.add(base if count == 0 else f"{base}-{count}")
        seen[base] = count + 1
    return result


def sections(text, prefix, label, errors):
    body, _ = prose(text)
    result = {}
    for block in re.split(r"(?=^## )", body, flags=re.M):
        heading = re.match(rf"^## ({prefix}[1-9]\d*)\s*\n", block)
        if not heading:
            if re.match(rf"^## {prefix}\d", block):
                errors.append(f"{label}: invalid {prefix}-numbered heading")
            continue
        identifier = heading.group(1)
        if identifier in result:
            errors.append(f"{label}: duplicate {identifier}")
        result[identifier] = block
    return result


def fields(block, names, label, errors):
    result = {}
    for name in names:
        values = re.findall(rf"^- {re.escape(name)}: *(.*)$", block, re.M)
        if len(values) != 1 or not values[0].strip():
            errors.append(f"{label}: expected one nonempty {name} field")
        result[name] = values[0].strip() if values else ""
    return result


def requirement_refs(text, source, known, label, errors):
    refs = set()
    for identifier, target in link_values(REQUIREMENT_LINK, text):
        if target != f"{source}#{identifier.lower()}" or identifier not in known:
            errors.append(f"{label}: invalid requirement reference {identifier} ({target})")
        else:
            refs.add(identifier)
    return refs


def feature_specs(root, errors):
    base = root / "docs/specs"
    if not base.is_dir():
        return 0
    bundles = [p for p in sorted(base.iterdir()) if p.is_dir() and not p.name.startswith(".")]
    for bundle in bundles:
        label = str(bundle.relative_to(root))
        sources = [name for name in ("requirements.md", "bugfix.md") if (bundle / name).is_file()]
        missing = [name for name in ("design.md", "tasks.md", "activity.md") if not (bundle / name).is_file()]
        if len(sources) != 1:
            errors.append(f"{label}: expected exactly one requirements.md or bugfix.md")
        for name in missing:
            errors.append(f"{label}: missing bundle file {name}")
        if len(sources) != 1 or missing:
            continue
        source = sources[0]
        requirements = sections((bundle / source).read_text(encoding="utf-8"), "R", label, errors)
        if not requirements:
            errors.append(f"{label}: no R-numbered requirements")
        for identifier, block in requirements.items():
            if not block.split("\n", 1)[1].strip():
                errors.append(f"{label}: empty requirement {identifier}")
            for name in ("Behavior", "Acceptance"):
                values = re.findall(rf"^{name}: *(.*)$", block, re.M)
                if len(values) != 1 or not values[0].strip():
                    errors.append(f"{label}/{identifier}: expected one nonempty {name} paragraph")

        design, _ = prose((bundle / "design.md").read_text(encoding="utf-8"))
        covered = requirement_refs(design, source, requirements, f"{label}/design.md", errors)
        for identifier in requirements.keys() - covered:
            errors.append(f"{label}/design.md: requirement {identifier} has no design link")

        blocks = sections((bundle / "tasks.md").read_text(encoding="utf-8"), "T", label, errors)
        tasks = {identifier: fields(block, TASK_FIELDS, f"{label}/{identifier}", errors)
                 for identifier, block in blocks.items()}
        if not tasks:
            errors.append(f"{label}: no T-numbered tasks")
        evidence_blocks = sections((bundle / "activity.md").read_text(encoding="utf-8"), "E", label, errors)
        evidence = {identifier.lower(): fields(block, EVIDENCE_FIELDS, f"{label}/{identifier}", errors)
                    for identifier, block in evidence_blocks.items()}
        for identifier, record in evidence.items():
            if record["Task"] not in tasks:
                errors.append(f"{label}/{identifier}: evidence names unknown task {record['Task']!r}")
            if record["Result"] not in {"PASS", "FAIL", "PENDING"}:
                errors.append(f"{label}/{identifier}: invalid evidence result {record['Result']!r}")
        all_refs = set()
        dependencies = {}
        for identifier, task in tasks.items():
            task_label = f"{label}/{identifier}"
            refs = requirement_refs(task["Requirements"], source, requirements, task_label, errors)
            all_refs.update(refs)
            if not refs:
                errors.append(f"{task_label}: no valid requirement links")
            dependency = task["Depends on"]
            deps = [] if dependency == "none" else [value.strip() for value in dependency.split(",")]
            dependencies[identifier] = deps
            for dep in deps:
                if dep not in tasks:
                    errors.append(f"{task_label}: unknown dependency {dep!r}")
            state = task["Verification state"]
            if state not in {"PASS", "FAIL", "PENDING"}:
                errors.append(f"{task_label}: invalid verification state {state!r}")
            record_links = [reference for (reference,) in link_values(EVIDENCE_LINK, task["Evidence"])]
            if task["Evidence"] != "PENDING" and not record_links:
                errors.append(f"{task_label}: evidence must link to an E record in activity.md")
            for reference in record_links:
                record = evidence.get(reference)
                if not record or record["Task"] != identifier:
                    errors.append(f"{task_label}: evidence {reference} missing or belongs to another task")
            if state == "PASS":
                if not record_links:
                    errors.append(f"{task_label}: PASS requires linked evidence")
                for reference in record_links:
                    record = evidence.get(reference)
                    if not record:
                        continue
                    if record["Result"] != "PASS":
                        errors.append(f"{task_label}: PASS evidence result is not PASS")
                    for name in EVIDENCE_FIELDS:
                        value = record[name]
                        if not value or value.upper() in {"PENDING", "UNKNOWN", "UNKNOWN/PENDING", "UNRECORDED", "TBD"} or PLACEHOLDER.search(value):
                            errors.append(f"{task_label}: PASS evidence has unresolved {name}")
                for dep in deps:
                    if dep in tasks and tasks[dep]["Verification state"] != "PASS":
                        errors.append(f"{task_label}: PASS has unverified dependency {dep}")
        for identifier in requirements.keys() - all_refs:
            errors.append(f"{label}/tasks.md: requirement {identifier} has no task coverage")

        visited = set()
        visiting = set()

        def visit(identifier):
            if identifier in visiting:
                errors.append(f"{label}: dependency cycle involving {identifier}")
                return
            if identifier in visited:
                return
            visiting.add(identifier)
            for dependency in dependencies[identifier]:
                if dependency in tasks:
                    visit(dependency)
            visiting.remove(identifier)
            visited.add(identifier)

        for identifier in tasks:
            visit(identifier)
    return len(bundles)


def validate(root=ROOT):
    root = Path(root).resolve()
    errors = [f"missing required path: {name}" for name in REQUIRED if not (root / name).is_file()]
    docs = sorted(p for p in root.rglob("*.md") if ".git" not in p.relative_to(root).parts)
    link_count = 0
    for path in docs:
        relative = path.relative_to(root)
        text = path.read_text(encoding="utf-8")
        body, open_fence = prose(text)
        if open_fence:
            errors.append(f"{relative}: unclosed fenced block")
        for number, line in enumerate(text.splitlines(), 1):
            if line.rstrip() != line:
                errors.append(f"{relative}:{number}: trailing whitespace")
        for (target,) in link_values(LINK, body, allow_images=True):
            target = target.removeprefix("<").removesuffix(">")
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("//"):
                continue
            # Link placeholders are intentional until the generated project is configured.
            if PLACEHOLDER.search(target):
                continue
            location, _, fragment = target.partition("#")
            location = unquote(location.split("?", 1)[0])
            destination = (path.parent / location).resolve() if location else path
            link_count += 1
            if not destination.is_relative_to(root):
                errors.append(f"{relative}: local link leaves the repository: {target}")
            elif not destination.exists():
                errors.append(f"{relative}: missing local link target: {target}")
            elif fragment and destination.suffix == ".md":
                if unquote(fragment) not in anchors(destination.read_text(encoding="utf-8")):
                    errors.append(f"{relative}: missing heading anchor: {target}")
        unquoted = without_inline_code(body)
        if PLACEHOLDER.search(unquoted):
            errors.append(f"{relative}: wrap prose placeholders in code spans so Markdown preserves them")

    bundle_count = feature_specs(root, errors)
    starter = root / ".github/workflows/ci.yml.example"
    workflow = root / "WORKFLOW.md"
    if starter.is_file() and workflow.is_file():
        if "lint-test-build:" not in starter.read_text(encoding="utf-8"):
            errors.append("CI starter: expected lint-test-build job")
        for reference in (".github/workflows/ci.yml.example", ".github/workflows/ci.yml", "lint-test-build"):
            if reference not in workflow.read_text(encoding="utf-8"):
                errors.append(f"WORKFLOW.md: missing CI reference: {reference}")
        readme = root / "README.md"
        if readme.is_file() and ".github/workflows/ci.yml.example" not in readme.read_text(encoding="utf-8"):
            errors.append("README.md: missing CI starter reference")

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"PASS: {len(docs)} Markdown files, {link_count} local links/anchors, {bundle_count} feature bundles; required paths, traceability, dependencies, evidence, placeholders, and CI references.")
    return 0


if __name__ == "__main__":
    raise SystemExit(validate())
