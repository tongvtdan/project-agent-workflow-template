# CLAUDE.md

Claude Code should use this file for tool-specific orientation, then follow [AGENTS.md](AGENTS.md) as the project contract.

## Project

- Product: `<Project Name>`
- Internal codename: `<Codename or same as product>`
- Main app: `<app_folder>/`
- Issue tracker: GitHub Issues, repo `<org>/<repo>` (`https://github.com/<org>/<repo>/issues`)

## Claude Operating Rules

- Start from the user outcome, not the requested implementation detail.
- Keep changes small, local, and verifiable.
- Prefer existing framework, state, data, and UI patterns over new abstractions.
- Route user-facing copy through the project localization/copy system.
- Keep sensitive, health, finance, legal, or AI-generated claims conservative and explainable.
- Do not rebuild explicitly deferred product concepts from `AGENTS.md` or `DESIGN.md`.
- Open or update a PR against the issue's feature branch rather than committing straight to `main`.

## Commands

Run from `<app_folder>/`:

```sh
<install command>
<analyze/lint command>
<test command>
<run command>
<codegen command if applicable>
```

## Highest-Leverage Work

Prefer work that improves one of:

- first-session activation
- recurring retention
- core data trust
- subscription or direct revenue conversion
- distribution artifact or share loop

Current product priority:

```text
<first value path>
```

## Handoff Format

For meaningful work, end with:

```text
Insight:
Decision:
Execution:
Verification:
Risk / next:
```
