# Extract API Request

## Endpoint
**POST** `https://extract.api.odoo.com/api/extract/parse`

## Parameters
*   `jsonrpc`: "2.0"
*   `method`: "call"
*   `params`:
    *   `account_token`: String. Your IAP token.
    *   `db_uuid`: String. Unique ID of the database.
    *   `documents`: List of Strings. Base64 encoded content of files to process.
    *   `user_infos`: Dict. Optional metadata (user email, etc.).

## Python Example (Internal)
Odoo uses `iap.jsonrpc` to call this.

```python
result = iap_tools.iap_jsonrpc(
    'https://extract.api.odoo.com/api/extract/parse',
    params={
        'account_token': token,
        'documents': [base64_data],
    }
)
```
