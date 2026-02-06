# Error management (ORM API)

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/orm.html

## TL;DR

- Utiliser les exceptions Odoo (`UserError`, `ValidationError`, `AccessError`) pour feedback UI correct.
- Ne pas masquer les erreurs avec `except Exception: pass`.

## Concepts clés

- Validation métier : `ValidationError` (contraintes).
- Erreurs utilisateur : `UserError` (message clair).
- Droits : `AccessError` (sécurité).

## Patterns recommandés

- Messages courts, actionnables, sans détails internes.
- Logger (`_logger.exception`) quand on relance une erreur inattendue.

## Pièges fréquents

- Lever une exception générique → UI/HTTP pas toujours propre.
- Message trop technique → support difficile.

## Exemples

```python
from odoo.exceptions import UserError, ValidationError

if not rec.partner_id:
    raise UserError("Veuillez choisir un client.")

if rec.amount < 0:
    raise ValidationError("Le montant doit être positif.")
```
