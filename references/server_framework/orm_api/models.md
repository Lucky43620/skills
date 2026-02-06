# Models (ORM API)

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/orm.html

## TL;DR

- Définis un modèle via une classe Python (`models.Model` / `TransientModel` / `AbstractModel`).
- Les champs sont des attributs de classe (attention collisions champ/méthode).
- Le recordset est l’unité de travail : méthodes appelées sur `self` (multi-record).

## Concepts clés

- `_name`, `_description`, `_inherit`, `_inherits` (héritage / extension / composition).
- `_rec_name`, `_order`, `_check_company_auto`, `_parent_store` (arborescences).
- Modèles persistants vs transients (vacuum) vs abstraits.

## Patterns recommandés

- Toujours écrire les méthodes ORM en supportant `self` multi-record (boucle `for rec in self:`).
- Utiliser `ensure_one()` quand la logique exige un seul enregistrement.
- Préférer des champs stockés + index adaptés quand la recherche est fréquente.

## Pièges fréquents

- Champ et méthode avec le même nom : le dernier défini écrase l’autre sans erreur visible.
- Oublier `@api.depends` sur un compute (recalcul incomplet / non déclenché).
- Utiliser des variables globales mutables (multi-db dans un même process).

## Checklist

- [ ] Créer `models/__init__.py` + importer le fichier du modèle.
- [ ] Ajouter `security/ir.model.access.csv`.
- [ ] Ajouter views + action + menu, et déclarer dans `__manifest__.py`.
- [ ] Tester création/édition + droits sur un utilisateur non-admin.

## Exemples

```python
from odoo import models, fields, api

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Property'
    _order = 'id desc'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    expected_price = fields.Float()

    @api.depends('expected_price')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.name} ({rec.expected_price})"
```

## Voir aussi

- `assets/templates/server/orm_model.py` (template)
- ../security_in_odoo/access_rights.md
- ../../02_playbooks/WORLDFLOWS.md
