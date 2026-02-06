# Inheritance and extension (ORM API)

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/orm.html

## TL;DR

- Deux axes : héritage Python (`_inherit`) et composition (`_inherits`).
- Extension “in-place” : `_inherit='model.name'` sans `_name`.
- Héritage multiple possible; attention collisions.

## Concepts clés

- `_inherit` (extension/héritage) vs `_inherits` (composition via m2o).
- Surcouches : override méthode + `super()`.
- Données : héritage de views, actions, sécurité en parallèle.

## Patterns recommandés

- Ajouter des champs/méthodes via extension in-place quand tu veux enrichir un modèle existant.
- Préférer `_inherits` quand tu veux exposer les champs d’un modèle parent tout en stockant séparément.
- Sur override : toujours appeler `super()` sauf raison explicite et documentée.

## Pièges fréquents

- Oublier de gérer `super()` (casse logique standard).
- Collisions de noms de champs (surtout avec `_inherits`).

## Exemples

```python
# Extension in-place
from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_code = fields.Char()
```

```python
# Composition
class X(models.Model):
    _name = 'x.model'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', required=True, ondelete='cascade')
```
