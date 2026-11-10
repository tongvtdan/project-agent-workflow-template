# Feature specifications

Use a feature bundle when work spans multiple tasks, sessions, or architectural boundaries. For a small agreed fix, keep the same outcome, failure case, and verification in the issue instead of creating four documents.

The flow is requirements (or bug analysis) → technical design → tasks → implementation and verification → review packet → authorized merge.

## Sources of truth

| Artifact | Owns |
| --- | --- |
| Root [SPEC.md](../../SPEC.md) | Feature index and issue-sized scope |
| Root [DESIGN.md](../../DESIGN.md) | Visual system, tokens, copy, accessibility |
| Feature requirements.md or bugfix.md | Accepted behavior, exclusions, acceptance IDs |
| Feature design.md | Technical decisions, interfaces, data flow, failure handling, verification strategy |
| Feature tasks.md | Task contracts, dependencies, and evidence links |
| Feature activity.md | Append-only decisions, attempts, actual checks/results, candidate references |
| GitHub issue/board selected in [WORKFLOW.md](../../WORKFLOW.md) | Authoritative issue status |
| [PROJECT_STATE.md](../../PROJECT_STATE.md) | Active feature/task pointer, current candidate, blockers, next action |

Do not maintain another issue-status ledger in tasks.md. Its verification state describes the task evidence, not whether a GitHub issue is closed or a release is approved. Keep only the active pointer in project state; link to the detailed artifacts.

## Create a bundle

Create one folder directly under docs/specs/ using a descriptive feature slug. Copy [Trail Log offline save](trail-log-offline-save/requirements.md) as an explicitly fictional example, then replace its facts. A bundle contains exactly one of requirements.md or bugfix.md, plus design.md, tasks.md, and activity.md.

In requirements.md, use H2 headings R1, R2, and so on. Under each heading include one Behavior: paragraph and one Acceptance: paragraph, each beginning on its own line. State observable behavior and a concrete acceptance check. Include normal, boundary, and realistic failure paths. Resolve consequential ambiguity before implementation; preserve accepted intent rather than rewriting it to fit a bug.

For bugfix.md, record current behavior/reproducer, expected behavior, and behavior that must remain unchanged. Express the expected and unchanged behavior under the same R-numbered headings so design and tasks can trace to them.

## Technical design

Reference every requirement using an ordinary local Markdown link, for example [R1](trail-log-offline-save/requirements.md#r1). Inside a bundle, link to its own requirements.md or bugfix.md. Include owning paths/interfaces, data flow, persistence/migration boundaries, failure states, and checks. Link to root DESIGN.md for visual rules.

Traceability/evidence references must be ordinary clickable links. Code-formatted examples, escaped bracket text, and image labels are not requirement or evidence links.

Do not introduce a new architecture to fill a diagram. Record the smallest viable design and important alternatives/decisions.

## Task format

Use H2 headings T1, T2, and so on; keep IDs stable even if a title changes. Under each heading include these one-line fields:

- Outcome: one independently verifiable result.
- Requirements: Markdown links whose labels and anchors match R IDs in this bundle.
- Depends on: none, or comma-separated task IDs such as T1, T2.
- Owner: responsible writer or reviewer; role assignment is not permission to spawn an agent.
- Scope: owning paths and explicit exclusions.
- Acceptance: observable normal/failure behavior for this task.
- Check: actual command or manual/device procedure to run.
- Verification state: PENDING, PASS, or FAIL.
- Evidence: PENDING, or a link to a matching E-numbered record in activity.md.
- Issue: verified issue reference, or UNLINKED. A parent feature issue can cover several small tasks.

Keep tasks small enough to implement and check in one focused session; split again if a task still has multiple unrelated outcomes. Estimate only when useful, and label estimates.

## Execute and resume

Within the authorized scope, choose tasks whose dependencies have PASS evidence. Research/test-only tasks can precede implementation. Run the check, record evidence, then update the task's verification state. A failed check is FAIL; an unperformed check, unavailable reviewer, or missing physical evidence is PENDING.

Update related artifacts when new evidence changes the plan; append why in activity.md. Retry a failing mechanism only with new information; after two unsuccessful attempts, gather the missing observation or revise the plan. Preserve unrelated work; never use destructive resets as an automatic retry strategy.

On resume or after compaction, read PROJECT_STATE.md, the active bundle, and recent activity. Verify consequential claims against files, candidate identity, and actual results. Changed code invalidates affected evidence; reassess before carrying PASS forward. The validator checks structure, not whether a command actually ran or the evidence remains current.

One writer owns shared artifacts. Parallelize independent investigation or isolated work only when authorized, with dependencies and ownership explicit. Reviewers return evidence to the coordinator; they do not mutate the shared state or delegate further.

## Activity and evidence

Append dated decisions and attempts; do not rewrite history. A verified run record uses an H2 E ID such as E1 and these fields:

- Task: matching T ID.
- Timestamp: actual date/time/timezone.
- Candidate: checked commit or artifact version.
- Environment: relevant runtime/device/tool versions.
- Procedure: exact command or reproducible manual steps.
- Result: PASS, FAIL, or PENDING.
- Observation: actual output, exit code where applicable, expected-versus-observed behavior, and artifact links.

A task marked PASS must link to its own PASS evidence record and have passing dependencies. Do not substitute "tests passed" for the actual procedure/result. Preserve failed attempts when a later attempt succeeds. Never copy fictional results, secrets, raw patient/sensor data, or unrelated private details.

## Return a review packet

Use the existing PR description or /QA response, not a new competing review log:

1. Outcome and requirement/task links.
2. Checked candidate and changed artifacts/diff.
3. Acceptance PASS/FAIL/PENDING with evidence links.
4. Reproducible demonstration and expected result.
5. Findings, risks, pending physical/external evidence.
6. Required review and one decision/next action.

Required review that errors or is unavailable remains PENDING; it is never converted into PASS. Task PASS, issue Done, human acceptance, merge, and release are separate decisions. Follow the existing gates in WORKFLOW.md.

## Background work

[Automation recipes](../automation.md) are documentation only. They install no scheduler, worker, hook, webhook, or bot. Register a real automation only under separate authorization.

This structure adapts the requirements/design/tasks pattern described in [Kiro Specs](https://kiro.dev/docs/specs/) to the existing project contracts. Background-run and review ideas were informed by [Crew features](https://kiro.dev/docs/crew/features/). These are design influences, not installed integrations.
