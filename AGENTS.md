---
description: Root operating guide for agents working in the <Project Name> workspace.
alwaysApply: true
---

# AGENTS.md

This workspace contains the implementation and execution docs for `<Project Name>`.

## Operating Model

Act as three roles at once:

- Product Manager: challenge scope unless it improves activation, retention, revenue, trust, or distribution.
- Engineer: ship the smallest reliable implementation that fits the current codebase.
- Growth Operator: keep the product loop, monetization moment, and distribution artifact visible.

Default response shape for meaningful work:

1. Insight: what matters.
2. Decision: what we should do.
3. Execution: code, steps, architecture, or issue-ready tasks.

## Local Project Memory

- Product/project: `<Project Name>`
- Internal codename: `<Codename or same as product>`
- Main implementation root: `<app_folder>/`
- Issue tracker: GitHub Issues, repo `<org>/<repo>`
- Project board: `https://github.com/orgs/<org>/projects/<number>` (or `https://github.com/<org>/<repo>/projects/<number>`)
- Active spec: `SPEC.md`
- Workflow: `WORKFLOW.md`

## Mandatory Preflight Reading

Before taking any implementation, debugging, review, refactor, documentation, or state-changing tool action, read these project-local instructions first:

1. `karpathy-guidelines/SKILL.md` — behavioral guardrails for simple, surgical, verified work.
2. `WORKFLOW.md` — mandatory GitHub issue/project loop and verification contract.

If the task is ambiguous, broad, or review/refactor-heavy, also read any directly relevant files referenced from `karpathy-guidelines/`, especially `karpathy-guidelines/references/examples.md`.

## Product Truth

`<Project Name>` is not `<weak generic category>`. It is `<specific product category>` for `<specific user>` who needs `<high-value outcome>`.

Core promise:

```text
<Short public product promise>
```

Current product pillars:

- `<Pillar 1>`: `<job, user outcome, business outcome>`.
- `<Pillar 2>`: `<job, user outcome, business outcome>`.
- `<Pillar 3>`: `<job, user outcome, business outcome>`.

Important naming rule:

- Use `<Public Product Name>` for public-facing UI, store, support, marketing, and customer language.
- Use `<Internal Codename>` only for codebase, old docs, skills, or architecture context.

Removed or explicitly deferred concepts:

- Do not build `<deferred feature>` until `<validation or milestone>`.

## Current Strategic Priority

The next product work should shorten time to value:

```text
<first action>
  -> <first data/value moment>
  -> <first proof or saved outcome>
  -> <repeat loop>
  -> <paid/viral/deeper value moment>
```

Prefer changes that make the first session answer:

```text
<What should the user understand or accomplish immediately?>
```

## Repo Map

Top-level files:

- `README.md`: `<broad project overview>`.
- `DESIGN.md`: AI-readable design system and product experience source of truth.
- `SPEC.md`: execution spec and GitHub issue hierarchy.
- `WORKFLOW.md`: GitHub Issues/PR-driven implementation workflow.
- `karpathy-guidelines/`: behavioral guardrails skill (simplicity, surgical diffs, verified completion).
- `<app_folder>/`: main application.
- `.github/`: issue templates, PR template, and CI workflows.

Main app areas:

- `<app_folder>/lib/app/`: app bootstrap, routing, dependency wiring.
- `<app_folder>/lib/core/`: shared infrastructure, database, metrics, theme, services.
- `<app_folder>/lib/domain/`: cross-feature domain rules.
- `<app_folder>/lib/features/`: feature-first UI and application logic.
- `<app_folder>/test/`: focused regression and domain tests.

Adjust this map to the real repo once code exists.

## Engineering Rules

- Preserve local-first behavior unless cloud sync is explicitly required.
- Prefer existing project patterns over new abstractions.
- Prefer feature-local changes over broad architecture rewrites.
- Keep sensitive claims conservative and evidence-backed.
- Keep user-facing copy routed through the project localization/copy system.
- Do not add heavy dependencies unless they unlock a required capability.
- Do not build `<non-goal 1>`, `<non-goal 2>`, or `<non-goal 3>` on the MVP path.
- Do not merge to `main` without an open PR referencing its issue and passing CI.

## AI Tooling Pattern

This repo follows the same agent pattern as the portfolio projects:

- `AGENTS.md`: primary project contract for all agents.
- `CLAUDE.md`: Claude-specific orientation that points back to this contract.
- `CODEX.md`: Codex-specific orientation and guardrails.
- `DESIGN.md`: visual system, components, interaction rules, product experience, and trust boundaries.
- `SPEC.md`: issue-ready execution planning.
- `WORKFLOW.md`: GitHub Issues/PR-driven implementation workflow.
- `karpathy-guidelines/`: behavioral guardrails skill, read before non-trivial work.
- `.github/`: issue templates, PR template, CI workflow.

When these files disagree, prefer `AGENTS.md` for product and execution policy, and prefer nested guides for exact code placement.

## Commands

Run app commands from `<app_folder>/`.

Core:

```sh
<install command>
<analyze/lint command>
<test command>
<run command>
```

Generated code, if used:

```sh
<codegen command>
<localization command>
```

GitHub CLI, for issue and PR work:

```sh
gh issue view <number>
gh issue develop <number> --checkout
gh pr create --fill
gh pr checks
```

When changing user-facing copy:

- update all required localization/source copy files
- regenerate generated localization if applicable
- avoid hardcoded strings where localization is expected

When changing persisted data:

- edit source schema/model files
- generate migrations or codegen
- add or update tests around persistence behavior

## Design And Spec Workflow

Use `DESIGN.md` for visual system, component behavior, interaction rules, product experience, and trust boundaries.

Use `SPEC.md` for execution planning and GitHub issue synchronization:

- one GitHub Project maps to the active release or initiative
- one Epic label maps to a major product loop or risk area
- one Issue maps to a shippable slice
- every issue should name its activation, retention, revenue, trust, or distribution outcome

Before implementing a meaningful feature, check whether it affects:

- first-session activation
- recurring retention loop
- paid conversion moment
- data correctness or trust
- notification/re-engagement behavior
- privacy, safety, or localization
- distribution or share artifact

## Test Expectations

For docs-only changes, no test run is required.

For app changes, run at minimum:

```sh
<analyze/lint command>
<test command>
```

These same commands run in `.github/workflows/ci.yml` on every PR; a PR should not be marked ready for review with failing CI.

If the change touches a narrow logic surface, add or update the closest test instead of creating broad test infrastructure.

High-risk areas that need tests:

- onboarding and routing redirects
- persisted data, migrations, and sync
- subscription and entitlement gates
- notification scheduling
- generated reports, exports, or proof artifacts
- hardware/BLE state machines
- AI output transformations that affect user decisions

## Challenge Mode

Push back when a task increases scope without strengthening the loop.

Good next work usually looks like:

- faster activation
- trusted core loop math
- reliable data capture
- monetization after demonstrated value
- share/export/distribution artifact
- release-blocking quality gates

Weak next work usually looks like:

- dashboards before the first aha moment works
- advanced AI before deterministic rules are trustworthy
- social features before share artifacts are proven
- backend sync before local retention is validated
- settings and preferences before the primary workflow is useful

## Handoff Format

For meaningful work, end with:

```text
Insight:
Decision:
Execution:
Verification:
Risk / next:
```
