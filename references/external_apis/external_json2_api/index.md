# External JSON-2 API

> [!NOTE]
> **New in Odoo 19.**
> This is the recommended API for all new integrations.

## Overview
The JSON-2 API allows interacting with Odoo using standard JSON payloads. It replaces the legacy XML-RPC API.

## Built-in Documentation
Odoo 19 includes a built-in API documentation and testing tool.
*   **URL:** `https://<your-instance>/doc`
*   **Access:** Requires "Technical Documentation" user group.
*   **Features:**
    *   Browse all models and methods.
    *   Test API calls directly in the browser.
    *   Generate code snippets (Python, JSON).

## Endpoint
**POST** `/json/2`

## Authentication
Authentication is done via **API Keys**.
1.  Go to User Preferences.
2.  Account Security > Developer API Keys.
3.  Generate a new key.

## Request Format
```json
{
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "service": "object",
        "method": "execute_kw",
        "args": [...]
    },
    "id": 1
}
```
