# Web Controllers (`http.Controller`)

Controllers handle HTTP requests (routes) in Odoo.

## Definition
Inherit from `odoo.http.Controller`.

```python
from odoo import http

class MyController(http.Controller):
    @http.route('/my_module/hello', auth='public', type='http', website=True)
    def hello(self, name='World'):
        return f"Hello, {name}!"
```

## Decorator: `@http.route`
*   **route**: The URL path (e.g., `/shop/cart`).
*   **auth**: Access level.
    *   `public`: Anyone.
    *   `user`: Logged-in users.
    *   `none`: No session check (rare).
*   **type**:
    *   `http`: Returns HTML/Text/Response object. Arguments from query params/form data.
    *   `json`: Returns JSON. Arguments from JSON body. Used for RPC.
*   **website**: `True` if this page is part of the website (loads website menus, branding).

## Returning Responses
*   **String:** Simple text/html.
*   **`request.render`:** Render a QWeb template.
    ```python
    return http.request.render('my_module.template_id', {'key': 'value'})
    ```
*   **`request.redirect`:** Redirect to another URL.
