# Avoid throwing errors as much as possible

In the Odoo Web Client, throwing an Error usually results in a crash dialog (blocking the UI), which breaks the flow.

## Best Practices
1.  **Use Notifications for Business warnings:**
    Instead of `throw new Error("Invalid number")`, use:
    ```javascript
    this.notification.add("Invalid number", { type: "warning" });
    ```
2.  **Return status codes:**
    For internal utility functions, return `true/false` or `null` instead of throwing, if the failure is expected.
3.  **Recover gracefully:**
    If a component fails to load, render a Fallback UI instead of crashing the whole interface.
