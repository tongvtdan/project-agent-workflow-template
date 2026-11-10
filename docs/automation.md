# Proactive work recipes

Status: DOCUMENTED ONLY. Registration: NOT CONFIGURED.

These recipes describe possible future scheduled work. No bot, schedule, event trigger, webhook, or persistent worker is installed or started by this template. A documentation edit, feature plan, /Team request, or recipe does not authorize registration or execution.

## Common recipe contract

Before registration choose the actual project/repository, purpose, trigger/cadence and timezone, source access, runtime, permissions, result destination, time/cost budget, duplicate-notification rule, owner, and stop condition. Test the prompt manually first under its permitted scope.

Use ordinary CI for deterministic checks. Use an agent when interpreting logs or prioritizing findings adds value. A local job needs an available host/runtime; a document cannot keep a sleeping computer running. Verify the selected platform's current behavior and access at registration.

## Recipe: project health review

- Purpose: surface the one actionable blocker affecting the active project outcome.
- Proposed trigger: owner-selected periodic schedule; no schedule is configured.
- Inputs: active feature pointer, task/evidence links, accessible issues/PRs, CI results.
- Permissions: inspect only. Do not edit code, task state, issues, PR comments, or external records.
- Procedure: inspect current evidence; identify failed checks, unresolved feedback, stale candidate evidence, or a decision needed from the owner. Distinguish an actual failure from unavailable access.
- Output: observation/evidence, affected requirement/task/issue/PR, recommended next step, decision required or none.
- Destination: the review surface selected during registration; no destination is currently connected.
- Noise control: report only a new/materially changed actionable finding, using project + candidate + finding identity to deduplicate.
- Suggested budget: five minutes per run; choose any model/spend limit explicitly during registration.
- Stop: owner pauses/removes it, project is archived, or the registration's end date is reached. Access failures produce a bounded PENDING report, not an infinite retry loop.

## Recipe: bounded PR watch

- Purpose: return a specific PR when a new check/review result needs action.
- Proposed trigger: supported PR event or owner-selected periodic check; neither is registered.
- Inputs: one verified repository/PR, current head SHA, checks, and review threads.
- Permissions: inspect and report only. No replies, source fixes, pushes, thread resolutions, merges, or deploys.
- Output: changed result, exact PR/candidate, evidence links, review blocker, recommended next action.
- Destination: the owner-selected task/inbox/review surface.
- Noise control: one notification per material change; unchanged snapshots remain quiet.
- Suggested budget: five minutes per run and an owner-selected overall expiry.
- Stop: PR merged/closed, owner cancels, or expiry is reached. Record unavailable evidence as PENDING.

## Example output: fictional Trail Log

Illustrative report, not an executed run: offline-save task T2 cannot yet proceed because T1's failed-save reproduction has no recorded evidence. Recommended next action: reproduce the save failure and record the checked candidate and result. No actual finding, repository access, or notification is asserted here.

Return results in the [review-packet format](specs/README.md#return-a-review-packet). Keep durable feature evidence in its activity.md and current state in PROJECT_STATE.md only when a task explicitly authorizes those writes.

## Later registration

Use the platform's supported automation controls, preserve sandbox/approval policy, and record the actual registration ID and verified output destination. Do not put credentials in this file. Keep the recipes read-only unless the owner grants a new, explicit scope.

[Kiro scheduling](https://kiro.dev/docs/crew/features/cron/) distinguishes fixed schedules and change-oriented monitoring. [OpenAI scheduled tasks](https://learn.chatgpt.com/docs/automations?surface=app) describes supported scheduled-task surfaces and host requirements. Consult current documentation when registering; neither link establishes that anything is configured here.
