# Fields (ORM API)

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/orm.html

## TL;DR

- Les champs sont des descripteurs (`fields.*`) avec paramètres (string, required, readonly, index, default, groups…).
- Les champs relationnels (m2o/o2m/m2m) impactent fortement perf et sécurité.
- Les champs computed nécessitent `@api.depends` et parfois `store=True` + index.

## Concepts clés

- Champs simples: Char/Text/Integer/Float/Boolean/Date/Datetime/Selection.
- Relationnels: Many2one/One2many/Many2many, `ondelete`, commandes m2m (Command).
- Computed / inverse / related / company_dependent (property fields).
- Traductions : champs `translate=True` (valeurs stockées selon le mécanisme de version).

## Patterns recommandés

- Pour recherche fréquente: index adapté (`btree`, `trigram`, `btree_not_null`).
- Pour fields computed: `store=True` si filtré/trié en base, sinon éviter.
- Pour datetime: garder en UTC côté serveur; conversion gérée côté client.

## Pièges fréquents

- Mettre `readonly=True` et croire que ça bloque en backend (c’est UI seulement).
- Computed sans `depends` complet → incohérences.
- Écriture sur related/computed non inversable → erreurs.

## Checklist

- [ ] Définir libellé (`string`) + aide (`help`) pour UI.
- [ ] Revoir `copy`, `groups`, `company_dependent` si besoin.
- [ ] Si relationnel: définir `ondelete` et `check_company` si multi-société.

## Exemples

```python
from odoo import models, fields, api

class X(models.Model):
    _name = 'x.model'

    name = fields.Char(string="Nom", required=True, index=True)
    partner_id = fields.Many2one('res.partner', ondelete='restrict', check_company=True)
    tag_ids = fields.Many2many('x.tag')

    amount = fields.Float(default=0.0)
    amount_text = fields.Char(compute='_compute_amount_text', store=True)

    @api.depends('amount')
    def _compute_amount_text(self):
        for rec in self:
            rec.amount_text = f"{rec.amount:.2f}"
```

```python
# Many2many commandes (exemples)
# rec.tag_ids = [(6, 0, [1,2,3])]  # replace
# rec.tag_ids = [(4, 1)]          # add existing
# rec.tag_ids = [(3, 1)]          # remove
```

## Voir aussi

- `assets/templates/server/orm_constraints.py`
- constraints_and_indexes.md
- common_orm_methods.md
