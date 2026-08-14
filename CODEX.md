# CODEX.md

Codex should follow [AGENTS.md](AGENTS.md) first. This file exists so Codex, Claude, and other coding agents share the same project pattern without duplicating every rule.

## Project Memory

- Product: `<Project Name>`
- Internal codename: `<Codename or same as product>`
- Main app: `<app_folder>/`
- Active spec: `SPEC.md`
- Public promise: `<Short public promise>`
- Issue tracker: GitHub Issues + Projects, repo `<org>/<repo>`

## Operating Loop

For non-trivial work:

1. Define the user outcome and product loop impact.
2. Identify assumptions that affect data, privacy, safety, localization, persistence, monetization, or distribution.
3. Choose the smallest shippable implementation.
4. Edit only files connected to the outcome.
5. Verify with the narrowest meaningful test or command.
6. Open or update a pull request linked to the GitHub issue.
7. Report changed files, verification result, and residual risk.

## Architecture Guardrails

- Stack: `<Flutter/Riverpod/Drift/Supabase/RevenueCat/etc.>`.
- Keep the MVP local-first unless sync is explicitly required.
- Put UI in feature folders, state in application/provider code, durable data in repositories/DAOs/tables, and cross-feature rules in domain/core.
- Follow nearby code before adding new structure.
- Preserve localization and accessibility expectations.
- Keep optional data optional in both copy and logic.

## Product Guardrails

Every feature must improve at least one of:

- activation
- retention
- revenue
- trust
- distribution

Challenge work that adds:

- `<non-goal 1>`
- `<non-goal 2>`
- `<non-goal 3>`
- backend complexity before local value is validated
- AI or automation that does not create a concrete user action

## Issue Workflow

When working from a GitHub issue:

- assign the issue to yourself and add the `in-progress` label (or move it on the Project board) when starting
- create a branch named `<type>/<issue-number>-<short-slug>` (e.g. `feature/42-export-retry`)
- implement the smallest shippable slice
- open a PR that references the issue (`Closes #<number>`) with what changed, verification commands, pass/fail result, and follow-up risk
- request review; do not merge your own PR unless the repo owner has said solo-merge is allowed
- leave the issue open until the PR merges, then let the `Closes #<number>` keyword close it automatically

## Completion Format

```text
Insight:
Decision:
Execution:
Verification:
Risk / next:
```
