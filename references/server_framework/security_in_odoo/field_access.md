# Field Access

## TL;DR

- Accès champ : via `groups=` sur la définition de champ, et/ou via views (groups) côté UI.
- Complète ACL/rules en cachant ou limitant des champs sensibles.

## Patterns recommandés

- Mettre `groups` sur le champ si c’est une règle d’accès fondamentale.
- Mettre `groups` dans la vue si c’est purement UI (pas sécurité forte).

## Pièges fréquents

- Cacher un champ dans la vue ne le sécurise pas côté RPC/ORM.

## Exemples

```python
secret = fields.Char(groups="base.group_system")
```
