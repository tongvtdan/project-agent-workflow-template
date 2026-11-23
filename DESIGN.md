# UI and interaction guide

Fill this guide when a project has a user interface. Link to the implementation so a contributor can find the existing components, tokens and patterns. Technical architecture for a feature belongs in its [feature bundle](docs/specs/README.md).

| Decision | Project reference |
| --- | --- |
| Primary screen and user action | `<screen, user job, route or view path>` |
| Components and design tokens | `<source paths for components, colors, typography and spacing>` |
| Interaction and copy | `<patterns for input, feedback, retry, localization>` |
| Supported layouts and accessibility | `<device sizes, input methods and accessibility checks>` |

For the changed flow, describe what a user sees with empty data, during an operation, after success, and on failure. Use the actual supported inputs, viewport or device and assistive settings for verification.

**Trail Log example.** A hiker checks one item. Show saving until storage confirms the write. If it fails, keep the edit visible and offer Retry. Provide a text or accessible state for packed items alongside the visual checkmark. Check what the hiker sees after restart. [Worked example](examples/trail-log.md)
