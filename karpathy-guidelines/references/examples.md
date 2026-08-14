# Karpathy Guidelines Examples

These examples describe the project-wide anti-patterns this skill is meant to prevent. Replace the placeholder scenarios with real ones from `<Project Name>` once a few real incidents or review comments exist.

## Hidden Assumptions

Weak response: implement `<a change>` without checking whether it affects `<related case A>`, `<related case B>`, or `<related case C>`.

Better response: trace the change through all branches of `<the affected function>`, state which cases are covered, and flag any edge case that could flip the result silently.

## Over-Abstraction

Weak response: build a generic `<strategy/plugin/registry>` system to handle different `<input formats/variants>`.

Better response: add a branch inside `<the existing function>` for the specific case that needs handling. Extract only when three or more distinct real cases exist and the duplication becomes the actual problem.

## Drive-By Refactoring

Weak response: fix `<a specific bug>` while also renaming unrelated variables, reformatting the file, and reorganizing nearby components.

Better response: change only the lines needed to fix `<the specific bug>`, verify the fix, and leave all adjacent code intact. Note the unrelated cleanup opportunity in the handoff instead of doing it.

## Verifiable Goals

Weak response: "improve `<quality area>`" or "make `<feature>` more reliable" without a measurable path.

Better response: define the observable result (e.g., "`<concrete, measurable acceptance criterion>`"), run the closest check, and stop when that criterion is met.

## Crossing Architectural Boundaries

Weak response: move state into a new store/context/provider, or add a network call, when the user asks for `<a feature that sounds like it needs one>`.

Better response: keep state and persistence within the documented architectural boundaries (see `AGENTS.md`). Confirm the boundary is intentional before proposing anything that crosses it.

## Unsafe Correctness Defaults

Weak response: return the optimistic result (`<e.g. OK, valid, approved>`) when required inputs are missing or ambiguous, because "nothing has explicitly failed."

Better response: return the conservative result (`<e.g. OPEN, unknown, blocked>`) whenever the outcome cannot be determined. A false positive on a trust-critical output protects the person relying on the report.
