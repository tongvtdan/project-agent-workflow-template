# Codex quick-start

Open the repository root in Codex. The project's shared instructions live in [AGENTS.md](AGENTS.md). Codex discovers instruction files along the path from the project root to its working directory. An AGENTS.override.md in a directory takes precedence over its AGENTS.md.

Start a fresh session and ask: “From your loaded project instructions, what directory owns the work and which command checks it?” Compare the answer with the project command table. When starting inside a package, check its scoped guide too. When starting at the root and editing a nested package, open that package's instructions explicitly.

For unfinished work ask Codex to read [project state](PROJECT_STATE.md), inspect the current diff, and pick up the recorded next check. [Codex instruction discovery](https://developers.openai.com/codex/guides/agents-md)
