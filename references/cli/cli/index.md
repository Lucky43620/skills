# Odoo CLI (`odoo-bin`)

The command-line interface is accessed via `odoo-bin` (or `entrypoint.sh` in Docker).

## Common Commands

### Server
Run the Odoo server.
```bash
./odoo-bin -c odoo.conf
```

### Scaffold
Create a new module structure.
```bash
./odoo-bin scaffold my_module modules/
```

### Shell
Start an interactive Python shell with the Odoo environment loaded.
```bash
./odoo-bin shell -d mydb
>>> self.env['res.partner'].search_count([])
```

### Populate
Populate a database with test data.
```bash
./odoo-bin populate -d mydb --model res.partner --size medium
```

### Deploy
Deploy a module to a remote server (requires SSH/setup).
*(Obscure/Rarely used, prefer Git)*
