# Constraints and indexes (ORM API)

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/orm.html

## TL;DR

- Deux familles : contraintes SQL (rapides) et contraintes Python (`@api.constrains`).
- Les indexes améliorent les recherches, mais coûtent en écriture.
- Odoo v19 met en avant la déclaration de contraintes/index comme attributs de modèle (cf changelog).

## Concepts clés

- SQL constraints via `_sql_constraints` (unicité, checks simples).
- Contraintes Python : validation business avec `ValidationError`.
- Index : sur champs stockés, types possibles selon champ/usage (btree/trigram).

## Patterns recommandés

- Utiliser SQL pour invariants simples et stables.
- Utiliser Python pour règles conditionnelles / cross-fields.
- Mesurer le gain (profiling) avant d’ajouter beaucoup d’indexes.

## Pièges fréquents

- Contraintes Python trop lentes sur gros volumes (boucles + searches).
- Indexer un champ peu sélectif (faible bénéfice).

## Exemples

```python
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class X(models.Model):
    _name = 'x.model'

    name = fields.Char(required=True)
    value = fields.Integer()

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Le nom doit être unique.'),
        ('value_pos', 'check(value >= 0)', 'La valeur doit être positive.'),
    ]

    @api.constrains('name', 'value')
    def _check_name_value(self):
        for rec in self:
            if rec.name and rec.value and rec.name == str(rec.value):
                raise ValidationError("name ne doit pas être égal à value")
```

## Voir aussi

- changelog.md
- ../performance/profiling.md
