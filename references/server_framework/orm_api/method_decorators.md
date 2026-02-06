# Method decorators (ORM API)

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/orm.html

## TL;DR

- Les décorateurs `odoo.api` définissent le contexte d’appel (depends, constrains, onchange, model_create_multi…).
- Ils pilotent recompute, validation, comportement UI, perf create/write.

## Concepts clés

- `@api.depends`: dépendances compute (impact recomputation).
- `@api.constrains`: validations server-side.
- `@api.onchange`: pseudo-record UI; ne pas faire de CRUD.
- `@api.model`, `@api.model_create_multi`: conventions d’arguments/retour.

## Patterns recommandés

- Toujours lister les dépendances *réelles* dans `@api.depends`.
- Pour create en batch : utiliser `@api.model_create_multi` + `vals_list`.
- Dans onchange : assigner des champs, utiliser `update()`, pas `create()/write()`. 

## Pièges fréquents

- Oublier `depends` → compute non déclenché.
- Écrire une contrainte lente (search dans boucle) → perf dégradée.
- Dans onchange: appeler `write` (comportement indéfini).

## Exemples

```python
from odoo import api, models, fields

class X(models.Model):
    _name = 'x.model'
    a = fields.Integer()
    b = fields.Integer(compute='_compute_b', store=True)

    @api.depends('a')
    def _compute_b(self):
        for rec in self:
            rec.b = rec.a * 2

    @api.constrains('a')
    def _check_a(self):
        for rec in self:
            if rec.a < 0:
                raise ValidationError('a must be >= 0')
```
