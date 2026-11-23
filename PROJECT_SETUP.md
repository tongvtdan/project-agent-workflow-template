# Set up a coding project

Open the new project's folder in your coding agent and send this first request:

> Set up this project with me. Inspect the checkout and existing docs, then ask for the missing code source, tracker, and product brief. Use my answers to fill in the local project instructions and workflow. Finish with one first task and how we will check it.

## First conversation

Inspect the repository root, remotes, README, manifests, CI, and any existing brief. Summarize what you found. Ask the following questions together, skipping those the checkout or the user's request already answers.

| What you need | What to ask |
| --- | --- |
| Code source | “Is this the project checkout? If the code lives elsewhere, which repository URL or local folder should I use?” If the remote points to the starter or several repositories are involved, confirm the intended target and owning directory. |
| Work tracker | “Where do you track this work? Share the GitHub Issues repository, GitHub Project, Linear project or issue, or say ‘local only’.” If several tools are linked, identify which one owns task status. |
| Product intent | “Where is the current product requirements document (PRD), brief, or accepted issue? A file, link, or pasted excerpt works. If you're starting from an idea, who is it for, what should they be able to do first, and what can wait?” |
| First outcome | “Which result matters first, and what would you observe if it worked?” Propose an answer from the brief when possible. Ask about constraints only when they change that first task. |

If a linked source is inaccessible, record it as supplied but unread and ask for the relevant excerpt only if needed. A project can start in a local folder with a sentence of intent and no tracker. For an empty repo, mark build and test commands pending until the implementation establishes them.

## Finish setup

- In [AGENTS.md](AGENTS.md), record the code source, implementation root, product purpose, and pointer to the current brief. If there is no brief, use the owner's short description. Check the command table against the codebase and distinguish commands found from commands actually run.
- In [WORKFLOW.md](WORKFLOW.md), record the selected tracker and status authority, or “local request.” A supplied link identifies a source. Creating issues, posting comments or changing board state requires authority for that action.
- Return one ready-to-use first request with its acceptance check. Use [project state](PROJECT_STATE.md) when handing off unfinished work. Reuse the recorded answers in later sessions and revisit them when the project changes.

## Fictional Trail Log example

**Owner:** “The code is in this local checkout, under `app/`. We keep tasks in the Trail Log project in Linear. Our brief is `docs/product-brief.md`. First priority is keeping packed items checked after restart. Cloud sync can wait.”

**Setup result:** Record the checkout and brief in the project instructions, and Linear as the status authority in the workflow. Read the brief if available and inspect the app for its real commands. The example names a hypothetical file and tracker.

**First request:** “Reproduce packed items losing their checkmarks after restart. Save a two-item list with one item checked, restart the app, and compare the stored and restored flags. Report the first difference.” The expected result is the same two items with only the original item checked.

**Starting from scratch instead:** “I only have this folder. Trail Log helps hikers keep a packing list offline. No tracker or PRD yet.” Record that sentence as the brief and the local request as the tracker. Propose the first slice: save and reopen one checklist locally. Acceptance is restoring the same item and its checked state after reopening.
