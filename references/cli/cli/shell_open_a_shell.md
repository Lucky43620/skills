# Shell

The shell command opens an interactive Python prompt (REPL) with a ready-to-use Odoo environment.

## Usage
`./odoo-bin shell -d <database_name>`

## Variables
*   `env`: The environment of the default user (Admin).
*   `self`: Same as `env.user`.
*   `odoo`: The `odoo` package.

## Example Session
```python
>>> self.env.company.name
'My Company'
>>> self.env['res.users'].search([('login', '=', 'admin')])
res.users(2,)
>>> self.env.cr.commit() # Don't forget to commit if you make changes!
```

> [!CAUTION]
> The shell does **not** auto-commit. You must call `self.env.cr.commit()` to save changes.
