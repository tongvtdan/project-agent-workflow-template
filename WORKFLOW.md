# Coding workflow

Start with the authorized request. A local change can go from a request to a reviewed diff. If using GitHub, link the issue and PR. If using a tracker, choose one authority for task status.

| Project setting | Starting value |
| --- | --- |
| Tracking | Local request by default. For GitHub Issues, GitHub Projects or Linear, enter the repository or project reference and the field or labels that own status. |
| Base branch | Use the actual default branch. |
| Required checks and reviewers | Preserve existing repository protections. List the actual job names and owners here when configured. |

## Choose the starting point

| What you have | What to do first | Where to record it |
| --- | --- | --- |
| An unresolved product idea | Identify the user, current workaround, evidence and smallest decision. Ask the owner to settle consequential tradeoffs. | A short proposal in the request. [Optional research prompts](docs/delivery/reusable-requests.md) |
| An agreed change | Write the intended result, scope, normal case and a realistic failure case. | Request or issue |
| A reported bug | Reproduce against a named candidate and trace where expected and observed behavior diverge. | Request or bug report |
| Several dependent changes | Link accepted behavior, technical design, tasks and activity. Start with a dependency-ready task. | [Feature bundle](docs/specs/README.md) |

## Make and verify the change

1. Inspect the working tree, owning code, applicable instructions and commands. Keep one writer per shared artifact. Preserve unrelated edits. For a linked issue use a branch such as `fix/12-restore-packed-flags`.
2. Implement one verifiable change. Use the closest meaningful test plus a check that exercises the affected boundary end to end. State which components were real and which were simulated.
3. Record the candidate, working directory, command, exit status, and expected versus observed result. A command that exits nonzero fails even if its summary lists passing tests. Give each acceptance criterion a verdict of PASS, FAIL or PENDING. A missing manual, hardware or external check stays PENDING.
4. If a check passes while the reported symptom persists, collect an observation that distinguishes possible causes. In Trail Log, inspect the stored packed flag after saving and its decoded value on reload before changing more code.
5. Return the diff, acceptance evidence, unresolved findings and any decision needed. An unavailable required review stays PENDING. Describe who actually reviewed the change. Use the [handoff record](PROJECT_STATE.md) when work continues in another session.

These boundary and exit-status checks draw on the reported [AFK Pilot case study](https://github.com/phuryn/product-engineering/blob/65444f5140579916b965b8ee157e28728340a518/CASE-STUDIES.md#afk-pilot).

## GitHub, CI and release

When authorized, open a draft PR, link the actual issue, and move it to the configured review state when ready. Close the issue after acceptance and merge or explicit acceptance under project policy. Preserve branch protection, CI and human-review requirements. Require all configured checks to pass and at least one approval unless the owner explicitly allows solo merge. Mandatory human reviews still apply. Changes involving sensitive data, payments, entitlements, notifications, migrations, hardware or user-affecting AI decisions require human review. Keep existing protected-execution controls intact.

For application CI, configure the runtime, working directory, real commands and base branch in [.github/workflows/ci.yml.example](.github/workflows/ci.yml.example), rename it to `.github/workflows/ci.yml`, and verify the `lint-test-build` job before requiring it. Record the actual required checks here.

For a release involving multiple components, keep one ordered checklist for the candidate. For each component record its dependency, command or manual step, expected result, observed result, and evidence. Stop at a failed required step. Release assessment reports readiness. Publishing requires release authority.

[Proactive recipes](docs/automation.md) are documentation only.
