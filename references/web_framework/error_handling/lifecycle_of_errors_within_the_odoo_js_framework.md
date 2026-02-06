# Lifecycle of errors within the Odoo JS Framework

1.  **Throw:** An error is thrown (JS Error, RPC Error, or utility `unhandledRejection`).
2.  **Catch (Global):** The browser's global `window.onerror` or `unhandledrejection` logic catches it.
3.  **Error Service:** The `error` service intercepts it.
4.  **Handling:**
    *   If it's a known non-blocking error (e.g. "Validation Error"), show a warning notification.
    *   If it's a server 500/Traceback, show the **Error Dialog** with the traceback.
5.  **Logging:** The error is often logged to the console for debugging.
