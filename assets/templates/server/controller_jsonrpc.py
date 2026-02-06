# Template — Controller JSON-RPC 2 (Odoo v19)

```python
from odoo import http
from odoo.http import request

class MyJsonRpcController(http.Controller):

    @http.route("/my_addon/ping", type="jsonrpc", auth="user")
    def ping(self, **kwargs):
        return {"ok": True}
```

Notes:
- En v19, la doc mentionne le renommage des controllers `json` en `jsonrpc` (type).
- Le routing HTTP utilise le chemin, le champ `method` JSON-RPC est ignoré côté Odoo.
