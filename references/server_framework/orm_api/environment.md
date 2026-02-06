# Environment (ORM API)

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/orm.html

## TL;DR

- `self.env` encapsule le contexte d’exécution (db cursor, user, context, registry).
- À travers `env` : accès aux modèles (`env['res.partner']`), user, company, lang, context.

## Concepts clés

- `env.cr` (cursor SQL), `env.uid`, `env.user`, `env.company`, `env.companies`.
- `env.context` (dict) : clés fréquentes (`lang`, `tz`, `active_test`, etc.).
- Méthodes utilitaires : `env.ref(xmlid)`, `env['model'].browse()`.

## Patterns recommandés

- Utiliser `with_context()` pour adapter comportement sans global state.
- Utiliser `with_company()` / `with_user()` si on doit simuler un contexte.
- Pour récupérer un record par xmlid : `env.ref('module.xmlid')` (attention aux noupdate).

## Pièges fréquents

- Muter `env.context` directement (ne pas).
- Utiliser `sudo()` au lieu de corriger ACL/rules (risque sécurité).

## Exemples

```python
# accéder à un modèle
Partner = self.env['res.partner']
partners = Partner.search([('active', '=', True)], limit=10)
```

```python
# récupérer une vue ou un record par xmlid
view = self.env.ref('my_addon.view_x_form')
```

```python
# changer de contexte
records = self.with_context(active_test=False)
```
