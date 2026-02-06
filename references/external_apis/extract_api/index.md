# Extract API (OCR)

The Extract API allows digitizing documents (invoices, expenses) using Odoo's AI-based OCR engine.

## Endpoint
`https://extract.api.odoo.com`

## Flow
1.  **Parse:** Send a document PDF or Image to the API.
2.  **Wait/Poll:** The document is processed asynchronously.
3.  **Get Results:** Retrieve the structured data (vendor, total, date, lines).

## Integration
In Odoo, this is handled by the `iap` and `account` modules. Custom integrations can call the endpoint via JSON-RPC.

### JSON-RPC 2.0
The API uses standard JSON-RPC 2.0.

### Request
```json
{
    "jsonrpc": "2.0",
    "method": "parse",
    "params": {
        "account_token": "...",
        "files": ["base64_content..."]
    },
    "id": 1
}
```
