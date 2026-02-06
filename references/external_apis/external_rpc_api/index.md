# External RPC API (XML-RPC)

> [!WARNING]
> **Deprecated in Odoo 19.**
> The XML-RPC and original JSON-RPC APIs are deprecated and scheduled for removal in Odoo 20.
> New integrations should use the **External JSON-2 API** (`/json/2`).

## Overview
Odoo provides an XML-RPC interface that allows external programs to interact with the server. It supports three main services:
1.  **Common:** Authentication and version checks.
2.  **Object:** CRUD operations on models.
3.  **DB:** Database management (creation, drop, dump).

## Endpoints
*   `/xmlrpc/2/common`
*   `/xmlrpc/2/object`
*   `/xmlrpc/2/db`

## Python Example (xmlrpc.client)
```python
import xmlrpc.client

url = "http://localhost:8069"
db = "my_db"
username = "admin"
password = "apikey_..."

common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]])
```
