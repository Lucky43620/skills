# db - Manage a Database

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/cli.html

## TL;DR

- Commandes utilitaires DB : init/dump/load/duplicate/rename/drop.
- Très utile pour automatiser environnements de test et migrations.

## Exemples

```bash
./odoo-bin db dump -d mydb -f mydb.dump
./odoo-bin db load -d mydb_test -f mydb.dump
```
