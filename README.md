# Coding project starter

Give Codex, Claude Code, and Gemini CLI the same project instructions. Start with one task in plain language. The template includes a fictional packing-list app, [Trail Log](examples/trail-log.md), as a worked example.

## Start a project

1. Choose **Use this template** on GitHub, or copy the starter into a project, including the hidden `.github` directory if you use GitHub. When adopting it in an existing repository, merge the files with your current instructions and CI.
2. Open the new project root in your coding agent and follow the [first-run setup guide](PROJECT_SETUP.md). Start by saying **“Set up this project with me using PROJECT_SETUP.md.”** The agent inspects the checkout, asks for any missing code source, tracker and PRD or brief, and helps you choose the first task.
3. Confirm the working directory and test command in [AGENTS.md](AGENTS.md). Codex reads it directly. [Claude Code](CLAUDE.md) and [Gemini CLI](GEMINI.md) import it. Follow [the workflow](WORKFLOW.md) when you start the agreed task.

**Try the first request.** In the fictional Trail Log project: “Packed items lose their checkmarks after restart. Reproduce this with a two-item list, check one item, and compare the saved value with what loads after restart. Show me where the values first differ.” Replace that symptom with one from your implementation. The starter contains documentation and a template validator.

## Open a guide when you need it

| When | Read |
| --- | --- |
| Starting Codex or checking its instruction scope | [Codex quick-start](CODEX.md) |
| Working on a feature with several dependent tasks | [Feature index](SPEC.md) and [bundle format](docs/specs/README.md) |
| Changing user interface behavior | [Visual and interaction design](DESIGN.md) |
| Framing a product decision or writing a focused request | [Request examples and optional PM references](docs/delivery/reusable-requests.md) |
| Coordinating several contributors | [Writer and reviewer handoff](docs/delivery/development-team.md) |
| Adopting shortcut phrases or numbered chat titles | [Shortcuts](SHORTCUTS.md) or [optional naming convention](CHAT_NAMING.md) |
| Reviewing the size or risk of a change | [Coding guardrails](karpathy-guidelines/SKILL.md) |
| Exploring proactive reviews | [Documented recipes](docs/automation.md) |

If you adopt shortcuts or chat naming, add a link to the chosen convention in the shared project instructions. Plain-language tasks work with the default setup.

## Adopt or upgrade

Retain existing project commands, scoped instructions, required reviews, and CI protections. If you use chat naming, carry the existing prefix, source, inventory, and every historical or reserved assignment into the naming record before replacing the old state file. Keep a single authoritative ledger. The example names and task numbers are fictional.

The [app CI starter](.github/workflows/ci.yml.example) is opt-in. Configure it for the actual stack and default branch. A GitHub template copies repository files. Configure board links, check requirements, and integrations separately if you use them.

## Check the template itself

From the repository root run:

```sh
python3 scripts/validate_template.py
python3 -m unittest discover -s tests -v
git diff --check
```

These commands check the starter documents and their validation rules. To remove optional starter files in a generated project, update incoming links and adapt or retire the template validator, its fixture tests, and its template CI job together. Keep the project's application checks active.
