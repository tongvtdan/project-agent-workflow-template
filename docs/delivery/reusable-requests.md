# Requests for coding work

Give the agent an outcome, relevant files or symptom, scope, and a way to recognize success. Plain language works in each client. The [shortcut catalogue](../../SHORTCUTS.md) is optional.

| Situation | Fictional Trail Log request |
| --- | --- |
| Investigate a bug | “Packed items lose their checkmarks after restart. Reproduce with a two-item list and one checked item. Show where the stored and restored values first differ.” |
| Implement an agreed fix | “Fix the confirmed save/load mismatch and its direct callers. Preserve the last saved list on failure. Check restart and retry against the changed candidate.” |
| Verify or hand off | “Review the diff and actual results. Identify which boundary was exercised, what remains pending, and the next check another session can run.” |

## When the product decision is still open

Use one short brief: who has the problem, what they do today, what evidence supports a change, and what the owner needs to decide. Separate observed facts from assumptions. For example, before adding shared packing lists to Trail Log, find out how hikers coordinate packing today. A confirmed persistence bug already has a reproduction path.

The upstream PM pack offers these optional methods. They can inform a brief without installing a plugin.

| Question | Upstream skills |
| --- | --- |
| What stage are we at, and what decision is next? | `start-here`, `propose` |
| Which users experience the problem, and who should we serve first? | `market-segments`, `beachhead-segment` |
| What alternatives exist, and where should we outperform them? | `competitor-analysis`, `value-curve` |
| Why would someone switch, and what could bring the next user? | `value-proposition`, `growth-loops` |

[Product Engineering PM skills](https://github.com/phuryn/product-engineering/tree/65444f5140579916b965b8ee157e28728340a518/product)
