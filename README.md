# Project Agent Workflow Template

Use this repository when starting a product repo that will be worked on by AI coding agents and uses **GitHub Issues, Projects, Pull Requests, and Actions** as its workflow backbone.

The goal is to give every project a compact operating system:

- `AGENTS.md`: root contract for all agents.
- `CLAUDE.md`: Claude-specific orientation that points back to `AGENTS.md`.
- `CODEX.md`: Codex-specific orientation and implementation loop.
- `DESIGN.md`: AI-readable design system with tokens, components, UX rules, and product experience guardrails.
- `SPEC.md`: execution bridge for GitHub issues, sprints, and acceptance criteria.
- `WORKFLOW.md`: autonomous agent workflow template for a GitHub Issues/PR-driven loop.
- `app/AGENTS.md`: optional nested guide for the main app folder.
- `karpathy-guidelines/`: behavioral guardrails skill (simplicity, surgical diffs, verified completion) that agents read before non-trivial work.
- `.github/ISSUE_TEMPLATE/`: bug report and feature request issue templates.
- `.github/PULL_REQUEST_TEMPLATE.md`: PR description template tied to the issue workflow.
- `.github/workflows/ci.yml.example`: opt-in CI starter; rename it to `ci.yml` after configuring the runtime and commands.

## How To Use

1. Copy the files into a new project repo, including hidden files in `.github/` and the `karpathy-guidelines/` folder.
2. Replace every product, stack, repository, project-board, and command placeholder.
3. Configure `.github/workflows/ci.yml.example`, then rename it to `ci.yml` to enable CI. Delete it if the project is not ready for CI yet.
4. Delete sections and optional files that do not apply.
5. Keep root `AGENTS.md` as the highest-level product and execution contract.
6. Add nested `AGENTS.md` files only where commands, architecture, or safety rules differ.
7. Create or link the GitHub Project from the repo (see "Creating The GitHub Project" below) and fill in its URL in `AGENTS.md`, `SPEC.md`, and `WORKFLOW.md`.
8. Enable branch protection on `main` requiring the active CI checks and at least one review before merge.
9. If the coding agent supports MCP tools, install [code-review-graph](https://github.com/tirth8205/code-review-graph) and point it at the repo. It builds a queryable code graph (callers, dependents, test coverage) so agents can review changes and trace impact without reading whole files, which meaningfully cuts token usage on review- and refactor-heavy tasks.

Before the first commit, scan for unfinished setup:

```sh
rg -n '<[^>]+>|TODO|TBD|FIXME' .
```

Recommended placement:

```text
<project>/
  AGENTS.md
  CLAUDE.md
  CODEX.md
  DESIGN.md
  SPEC.md
  WORKFLOW.md
  <main_app_folder>/AGENTS.md
  karpathy-guidelines/
    SKILL.md
    references/
      examples.md
  .github/
    ISSUE_TEMPLATE/
      bug_report.md
      feature_request.md
    PULL_REQUEST_TEMPLATE.md
    workflows/
      ci.yml.example
```

## Creating The GitHub Project

`WORKFLOW.md` and `SPEC.md` assume a GitHub Project (the org/repo-level Kanban board, distinct from Issues themselves) already exists and is linked to the repo. Create it once per repo, using the [GitHub CLI](https://cli.github.com/) (`gh`):

```sh
# 1. Authenticate if needed
gh auth login

# 2. Create the Project (v2), owned by the org or user account
gh project create --owner <owner> --title "<Project Name> <release> - <initiative>"
# -> note the returned project number, used below as <project-number>

# 3. Link the project to this repo so issues/PRs can be added to it
gh project link <project-number> --owner <owner> --repo <owner>/<repo>

# 4. Add a Status field matching the statuses in SPEC.md (skip if it already exists)
gh project field-create <project-number> --owner <owner> \
  --name "Status" --data-type SINGLE_SELECT \
  --single-select-options "Backlog,Ready,In Progress,In Review,Done,Parked"
```

Equivalent manual steps: open `https://github.com/orgs/<owner>/projects` for an organization or `https://github.com/users/<owner>/projects` for a personal account -> **New project** -> **Link a repository** -> add a single-select **Status** field with the same options.

Once created, record the project URL (`https://github.com/orgs/<owner>/projects/<project-number>` or `https://github.com/users/<owner>/projects/<project-number>`) in `AGENTS.md` ("Local Project Memory"), `SPEC.md` ("Project URL"), and `WORKFLOW.md`, replacing the placeholders.

## Fill Order

1. `DESIGN.md`: decide visual tokens, components, interaction rules, product promise, user, loops, and non-goals.
2. `AGENTS.md`: convert those decisions into agent operating rules.
3. `SPEC.md`: turn the design into shippable GitHub issue slices.
4. `CODEX.md` and `CLAUDE.md`: keep tool-specific docs thin.
5. `WORKFLOW.md`: wire the GitHub Issues -> branch -> PR -> merge loop.
6. `karpathy-guidelines/`: fill in the real architectural boundaries, high-risk functions, and anti-pattern examples for this codebase.
7. `.github/`: fill in the issue templates, PR template, and CI commands for the real stack.
8. `<main_app_folder>/AGENTS.md`: add codebase-specific commands and placement rules.

## Rule Of Thumb

If a feature does not improve activation, retention, revenue, trust, or distribution, do not let agents build it by default. Challenge the scope and pick a smaller, higher-leverage slice.
