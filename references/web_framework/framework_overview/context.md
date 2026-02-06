# Context (JS)

The **Context** in Odoo JS is a plain object used to carry user preferences (language, timezone) and specific action parameters (default values, active filters) during RPC calls.

## Structure
A typical context object looks like:
```javascript
{
    "lang": "fr_FR",
    "tz": "Europe/Paris",
    "uid": 2,
    "allowed_company_ids": [1],
    "default_partner_id": 15,
    "active_id": 5,
    "active_model": "sale.order"
}
```

## Usage in RPC
When making calls to the server (ORM), the context is usually passed as a keyword argument.

```javascript
/* Using the ORM service */
await this.orm.call("res.partner", "search", [[["is_company", "=", true]]], {
    context: {
        ...this.user.context,
        default_is_company: true,
    },
});
```

## User Context
You can access the current user's global context via the `user` service.
```javascript
setup() {
    this.user = useService("user");
    console.log(this.user.context);
}
```
