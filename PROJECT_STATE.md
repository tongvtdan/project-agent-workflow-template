# Handoff for unfinished work

Update this record when another session needs to continue. A finished one-step change can use the normal review response. Link detailed attempts in the active feature or issue.

| Field | Current work |
| --- | --- |
| Updated / environment | `<date, timezone, workspace or device>` |
| Goal and authorized scope | `<observable outcome, allowed changes and exclusions>` |
| Active task and writer | `<request, issue or bundle/task link and current writer>` |
| Candidate | `<branch, commit or artifact version, relevant uncommitted paths>` |
| Changed / decided | `<affected artifacts and decision with reason>` |
| Evidence | `<criterion, PASS/FAIL/PENDING, check, exit status or observation, evidence link>` |
| Blocker or decision | `<what is missing, who can resolve it, required review>` |
| Next action | `<one step and its observable success condition>` |

**Resume prompt.** Read the shared and scoped instructions, this record, and the linked task. Compare the recorded candidate with the current branch, files and diff. Recheck affected evidence if they differ. Carry out the next authorized step and return its result. See the [Trail Log handoff](examples/trail-log.md#handoff-example).
