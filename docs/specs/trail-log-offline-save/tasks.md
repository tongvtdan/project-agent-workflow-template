# Trail Log offline save: task list

Fictional task contracts only. Verification is PENDING throughout; no commands have run for this app. GitHub owns live issue status once a real issue is linked. No GitHub issue is linked by this example.

## T1

- Outcome: reproduce save/load and failure behavior before choosing the storage correction.
- Requirements: [R1](requirements.md#r1), [R2](requirements.md#r2), [R3](requirements.md#r3), [R4](requirements.md#r4).
- Depends on: none
- Owner: implementation writer
- Scope: existing repository/storage boundary and focused tests; no UI redesign or new backend.
- Acceptance: capture two-item restart, empty-list, failed-write preservation, and retry observations.
- Check: inspect actual storage semantics; in a real Flutter app run the focused repository tests and a real save/restart reproduction.
- Verification state: PENDING
- Evidence: PENDING
- Issue: UNLINKED

## T2

- Outcome: preserve the intended checklist across successful save and restart.
- Requirements: [R1](requirements.md#r1), [R2](requirements.md#r2), [R3](requirements.md#r3).
- Depends on: T1
- Owner: implementation writer
- Scope: checklist repository/storage adapter and direct callers; no accounts, sync, or unrelated refactor.
- Acceptance: successful restore matches IDs/order/flags; failure preserves prior storage; retry does not duplicate.
- Check: run the real repository round-trip, injected-failure, and retry tests, then verify actual storage behavior.
- Verification state: PENDING
- Evidence: PENDING
- Issue: UNLINKED

## T3

- Outcome: show honest saving/saved/failure/empty feedback.
- Requirements: [R2](requirements.md#r2), [R4](requirements.md#r4).
- Depends on: T2
- Owner: implementation writer
- Scope: existing checklist screen/copy and closest UI tests; no global visual redesign.
- Acceptance: failed save keeps edits visible and offers Retry; an empty list offers its first action.
- Check: exercise the real UI's failure and empty-list states with accessibility/localization checks.
- Verification state: PENDING
- Evidence: PENDING
- Issue: UNLINKED

## T4

- Outcome: return a reviewable candidate with acceptance evidence and a restart demonstration.
- Requirements: [R1](requirements.md#r1), [R2](requirements.md#r2), [R3](requirements.md#r3), [R4](requirements.md#r4).
- Depends on: T2, T3
- Owner: coordinating agent; independent reviewer only when assigned and authorized
- Scope: candidate diff, relevant checks, demonstration, and review packet; no merge or release.
- Acceptance: each requirement has a verdict and evidence; required unavailable review remains PENDING.
- Check: run actual configured checks and the restart/failure/retry/empty-list walkthrough; return the review packet.
- Verification state: PENDING
- Evidence: PENDING
- Issue: UNLINKED
