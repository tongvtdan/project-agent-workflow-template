# Project instructions

On an initial setup request, follow [the first-run guide](PROJECT_SETUP.md) and configure this file for the project. All coding agents use it. Before editing a subdirectory, read the applicable scoped AGENTS.md files from the root to the target. The nearest guide supplies local placement and command details.

## Project facts

| Field | Fill from the actual repository |
| --- | --- |
| Code source and implementation root | `<repository URL or local folder and owning directory>` |
| Current PRD or brief | `<file, link, or owner-provided outcome if no separate brief>` |
| Purpose and user | `<who uses it and what outcome it provides>` |
| Stack and runtime versions | `<languages, frameworks, supported versions>` |
| Implementation and test locations | `<paths and responsibilities>` |
| Data or interface boundaries | `<owners of storage, APIs or generated files>` |
| Constraints | `<compatibility, privacy, non-goals, required reviewers>` |

## Commands

Use a path relative to the repository root for each working directory. Record verified commands or mark an operation inapplicable.

| Operation | Working directory | Command |
| --- | --- | --- |
| Install | `<directory>` | `<install command>` |
| Analyze or lint | `<directory>` | `<lint command>` |
| Targeted test | `<directory>` | `<test command>` |
| Run locally | `<directory>` | `<run command>` |
| Build | `<directory>` | `<build command>` |

## Working agreements

- Identify the observable outcome, scope, and acceptance check. Trace the owning code and its callers. Preserve existing user changes and follow the project's patterns.
- For a bug, reproduce the symptom before choosing a fix. For an agreed change, implement the smallest verifiable slice. Use [the workflow](WORKFLOW.md) for verification, review, and protected actions.
- Use the local request or linked issue for a small task. Open the [feature contract](docs/specs/README.md) for dependent work, and [UI guidance](DESIGN.md) for a visual change.
- Investigations and reviews are read-only unless the request also authorizes changes. Keep one writer per shared artifact. Commits, external writes, delegation, merges, and releases follow the authority of the task and project protections.
- Report what changed, the candidate checked, commands and results, and pending checks. Record unfinished work in [project state](PROJECT_STATE.md) for another session. Keep secrets and private user data out of evidence.
