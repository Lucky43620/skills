# server - Run the Server

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/cli.html

## TL;DR

- Lance le serveur Odoo (odoo-bin server) avec options de config, DB, logs, dev tools.
- C’est la commande la plus utilisée en dev et CI.

## Concepts clés

- Options DB: `-d`, `--db-filter`, `--db_host`, ...
- Addons: `--addons-path` (ordre important, enterprise avant custom).
- Dev: `--dev=all`, logs, reload, tests.

## Patterns recommandés

- Utiliser un fichier `.conf` pour standardiser les environnements.
- En dev: activer logs SQL et `--dev` selon besoin (sans le garder en prod).

## Pièges fréquents

- Addons-path mal ordonné → modules chargés incorrectement.
- Options dev activées en prod → perf/risques.

## Checklist

- [ ] Vérifier python env + dépendances.
- [ ] Vérifier DB accessible et bonne version.
- [ ] Vérifier addons-path.

## Exemples

```bash
./odoo-bin server -c odoo.conf -d mydb --dev=all
```

```ini
; odoo.conf
[options]
addons_path=/odoo/enterprise,/odoo/addons,/odoo/custom_addons
log_level=info
```


## Voir aussi

- configuration_file.md
- db_manage_a_database.md
