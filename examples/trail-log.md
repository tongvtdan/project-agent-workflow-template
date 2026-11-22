# Trail Log walkthrough

Trail Log is a fictional offline packing-list app. The files and observations below illustrate a coding workflow. Application checks are PENDING.

## First task

“Packed items lose their checkmarks after restart. Reproduce with a two-item list, mark one item packed, then reopen the list. Compare what was written with what was restored. Show me where the values first differ.”

Start from the request or a bug issue. Record the app candidate and environment. Use one packed item and one unpacked item so loading all flags with the same default is observable. Capture the item IDs and flags at save, in persistent storage, and after a real process restart. Those observations distinguish a write failure from a reload error.

## When the fix grows

If storage, retry and UI feedback need separate changes, use the [requirements](../docs/specs/trail-log-offline-save/requirements.md), [technical design](../docs/specs/trail-log-offline-save/design.md), [task list](../docs/specs/trail-log-offline-save/tasks.md) and [activity record](../docs/specs/trail-log-offline-save/activity.md). The example excludes accounts and cloud sync.

## Evidence to return

| Check | What to record for the actual candidate | Example state |
| --- | --- | --- |
| Repository round-trip | Commit and dirty paths, working directory, exact command, exit status, IDs/flags before and after. Identify any in-memory store. | PENDING |
| Process restart | Device or runtime, actual storage, terminate/relaunch steps and both restored flags. | PENDING |
| Failed save and retry | Injected error, last stored list, visible feedback, and item count on retry. | PENDING |

If only the in-memory check has passed, record its own result. Restart remains PENDING until observed. If the stored flag is true but the decoded flag is false, inspect reload mapping. If the stored flag is already false, inspect the write path. These are diagnostic branches, not observations about a real app.

## Handoff example

**Outgoing agent (Codex).** In [project state](../PROJECT_STATE.md), link the active task T1 and its activity record. Record the actual branch, commit, relevant dirty paths and what was checked. For this example the candidate is unrecorded, no implementation has run, and restart remains PENDING.

**Incoming agent (Claude Code or Gemini CLI).** “Resume Trail Log T1. Compare the recorded candidate with the current tree. Reproduce the two-item restart in the real app. Return the first boundary where the flags differ and the command result or manual observation.” The receiving agent can start from these repository records without the earlier chat.

## Chat naming example

Only when a project adopts the [optional naming convention](../CHAT_NAMING.md), use its confirmed prefix, inventory and existing reservations. In this fictional project a confirmed TL-X-01 keeps number 01 across a handoff. Another project needs its own confirmed prefix.
