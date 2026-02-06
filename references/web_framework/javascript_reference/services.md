# Services (JS Reference)

Services are long-lived singleton objects that provide features to the whole application.

## Core Services
*   **rpc:** Low-level HTTP JSON-RPC calls.
*   **orm:** High-level Record/Model handling.
*   **action:** Managing actions (window, server, client).
*   **user:** Info about the current user (context, permissions).
*   **router:** URL state management.
*   **notification:** Displaying toaster notifications.

## Accessing
In a component:
```javascript
setup() {
    this.rpc = useService("rpc");
    this.notification = useService("notification");
}
```
