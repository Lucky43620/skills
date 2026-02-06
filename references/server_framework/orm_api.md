# ORM API & Models

**Point central du backend Odoo.**
Cette section détaille comment définir la structure de données et interagir avec la base de données via le code Python.

## Sommaire

### 1. [Modèles et Structure](orm_api/models.md)
Définition des classes `Model`, `TransientModel`, `AbstractModel`.
- Attributs clés: `_name`, `_description`, `_inherit`...
- Contraintes SQL (`_sql_constraints`).

### 2. [Champs (Fields)](orm_api/fields.md)
Les colonnes de vos tables.
- Types de base: `Char`, `Integer`, `Float`, `Boolean`, `Date`.
- Relationnels: `Many2one`, `One2many`, `Many2many`.
- **Commandes d'écriture** (`Command.create`, `Command.update`...).
- Attributs: `compute`, `related`, `store`, `ondelete`.

### 3. [Environnement & Recordsets](orm_api/recordsets.md)
Manipulation des données en mémoire.
- `self.env`: Accès au user, context, cursor.
- `self`: Le Recordset (collection d'enregistrements).
- Opérations d'ensemble: `filtered`, `mapped`, `sorted`.

### 4. [Méthodes ORM](orm_api/common_orm_methods.md)
Le Cycle de vie des données.
- CRUD: `create`, `write`, `unlink`.
- Recherche: `search`, `search_count`, `browse`.
- Avancé: `read_group` (statistiques).

## Cheat Sheet Rapide

```python
# Recherche & Boucle
orders = self.env['sale.order'].search([('state', '=', 'draft')])
for order in orders:
    print(order.name)

# Création avec Command (recommandé v19)
from odoo import Command
self.env['res.partner'].create({
    'name': 'Nouveau Client',
    'child_ids': [
        Command.create({'name': 'Contact 1', 'type': 'contact'}),
    ]
})
```
