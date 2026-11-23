---
name: karpathy-guidelines
description: Behavioral guardrails for AI coding work. Use when writing, reviewing, debugging, refactoring, or planning code changes where the agent should avoid wrong assumptions, overengineering, drive-by edits, or unverifiable completion.
---

# Karpathy Guidelines

Use this skill as a quality gate for non-trivial `<Project Name>` coding, debugging, refactoring, review, or architecture work. Bias toward explicit assumptions, simple code, surgical diffs, and verified outcomes.

## Operating Loop

1. Define the user outcome and success criteria.
2. Surface assumptions that affect scope, data, safety, correctness, or fidelity of generated artifacts.
3. Choose the smallest implementation that satisfies the outcome.
4. Change only files and lines that trace to the request.
5. Verify with the narrowest meaningful test or command.
6. Report what changed, what passed, and any residual risk.

## Simplicity First

- Do not add speculative features, extension points, configuration systems, or new packages.
- Do not introduce an abstraction for a single caller unless it removes real local complexity.
- Prefer existing project patterns before new structure.
- Keep error handling grounded in realistic failure modes for the changed behavior.
- If the solution feels large relative to the request, reduce scope before editing.

## Surgical Changes

- Match surrounding style.
- Do not reformat, rename, or refactor adjacent code as a side effect.
- Remove unused code only when your change made it unused.
- Mention unrelated concerns in the final handoff instead of editing them.

## Architectural Boundaries

Use the boundaries and commands configured in root and scoped AGENTS.md. Check existing callers, storage formats and generated sources before changing an interface. For a new dependency, explain its maintenance cost and follow the project’s review rules.

## Correctness and verification

Derive checks from the behavior the user needs. Record what was exercised and keep an unobserved outcome pending. For a change spanning two components, verify the real handoff between them. If a passing test leaves the symptom in place, capture one observation that distinguishes the possible causes.

## Examples

Use the [Trail Log examples](references/examples.md) for focused changes, boundary checks, and evidence.
