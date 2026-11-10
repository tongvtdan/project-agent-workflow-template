# Trail Log offline save: technical design

Fictional proposal, not inspected implementation. Follow the real codebase and root [visual contract](../../../DESIGN.md) when adapting it.

## Decisions and traceability

| Requirement | Smallest proposed mechanism | Check |
| --- | --- | --- |
| [R1](requirements.md#r1) | Existing checklist repository owns serialization and restoration of IDs/order/flags | Repository round-trip plus app restart |
| [R2](requirements.md#r2) | Repository/storage adapter reports failed writes; preserve last committed storage value and keep edits visible | Inject failed write and reload last stored value |
| [R3](requirements.md#r3) | Save by stable list/item IDs, replacing the intended snapshot rather than appending duplicates | Fail, retry, reload, compare IDs and count |
| [R4](requirements.md#r4) | Empty collection remains a valid saved state | Load empty data and inspect the first action |

## Ownership and data flow

Checklist screen → existing checklist repository → existing local storage adapter. Loading follows the reverse path. UI state separates saving, saved, and failed-save feedback; core list rules remain independent of UI and network access.

Illustrative owning paths are app/lib/features/checklists/checklist_repository.dart and its direct screen caller. These files do not exist in this template.

The adapter's real write/replace semantics must be inspected before implementation. If it can partially overwrite saved data, choose its supported transaction/atomic replacement mechanism before claiming R2. Do not infer durability from an in-memory mock.

## Failure and verification strategy

Keep the prior saved snapshot intact on failure, expose Retry, and preserve the user's unsaved edits. Run focused repository failure/retry tests, then verify actual persistence and app restart. Use text as well as icons for feedback; apply existing accessibility/localization rules.

No schema migration is proposed in this fictional slice. If actual inspection reveals a schema change, revise this plan and its acceptance before implementing a migration.

See [task dependencies](tasks.md) and [actual evidence record](activity.md).
