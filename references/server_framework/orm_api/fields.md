# Fields (ORM API)

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/backend/orm.html#fields

## Champs de Base

| Type | Description | Paramètres Clés |
| :--- | :--- | :--- |
| `Boolean` | Booléen simple. | `default` |
| `Char` | Chaîne courte. | `size`, `trim`, `translate` |
| `Text` | Texte multiligne. | `translate` |
| `Integer` | Entier. | `group_operator` |
| `Float` | Décimal. | `digits` (tuple `(16,2)` ou `'Account'`) |
| `Monetary` | Montant avec devise. | `currency_field` (défaut `'currency_id'`) |
| `Html` | Contenu riche. | `sanitize`, `strip_style` |
| `Date` | Date (YYYY-MM-DD). | `default` (`fields.Date.today`) |
| `Datetime`| Timestamp UTC. | `default` (`fields.Datetime.now`) |
| `Binary` | Fichier/Image base64. | `attachment` (store as file default True) |
| `Selection`| Liste de choix. | `selection` (liste de tuples ou méthode) |
| `Image` | Image redimensionnable. | `max_width`, `max_height` |

## Champs Relationnels

### `Many2one`
Lien vers un seul enregistrement d'un autre modèle.
```python
partner_id = fields.Many2one('res.partner', string="Partenaire", ondelete='restrict')
```
- **comodel_name** (req): Modèle cible.
- **ondelete**: `'set null'` (défaut), `'restrict'`, `'cascade'`.
- **domain**: Filtre côté client (et serveur pour `write`).
- **delegate**: `True` pour l'héritage par délégation.

### `One2many`
Relation inverse d'un Many2one. Crée une "liste" d'enregistrements liés.
```python
line_ids = fields.One2many('my.line', 'order_id', string="Lignes")
```
- **comodel_name** (req): Modèle cible.
- **inverse_name** (req): Champ Many2one dans le modèle cible.
- **copy**: `True` (par défaut `False`) pour copier les lignes à la duplication.

### `Many2many`
Relation N-N. Crée une table intermédiaire.
```python
tag_ids = fields.Many2many('res.partner.category', string="Étiquettes")
```
- **comodel_name** (req): Modèle cible.
- **relation**: Nom de la table intermédiaire (optionnel).
- **column1**: Nom de la colonne ID modèle courant (optionnel).
- **column2**: Nom de la colonne ID modèle cible (optionnel).

## Opérations sur les champs X2Many (Command)
Depuis Odoo 15+, utilisez l'espace de noms `odoo.fields.Command` pour écrire dans les champs `One2many` et `Many2many`.
Cela remplace les tuples magiques `(0, 0, vals)`.

```python
from odoo import Command

# Création
vals = {
    'line_ids': [
        Command.create({'name': 'Nouveau'}),
        Command.create({'name': 'Autre'}),
    ]
}

# Mise à jour
vals = {
    'line_ids': [
        Command.update(line_id, {'qty': 5}),
        Command.link(existing_id),
        Command.delete(old_id),
        Command.clear(), # Supprime tout (M2M: délie, O2M: supprime)
        Command.set([1, 2, 3]), # Remplace tout par cette liste d'IDs
    ]
}
```

| Méthode | Tuple Legacy | Description |
| :--- | :--- | :--- |
| `Command.create(vals)` | `(0, 0, vals)` | Crée un nouvel enregistrement et le lie. |
| `Command.update(id, vals)` | `(1, id, vals)` | Modifie un enregistrement lié existant. |
| `Command.delete(id)` | `(2, id)` | Supprime le lien ET l'enregistrement (O2M) / Délit seulement (M2M legacy behavior, mais attention). |
| `Command.unlink(id)` | `(3, id)` | Supprime le lien (ne supprime pas l'enregistrement, change FK à Null en O2M). |
| `Command.link(id)` | `(4, id)` | Ajoute un lien vers un enregistrement existant. |
| `Command.clear()` | `(5, 0)` | Supprime tous les liens (et enregistrements si O2M + ondelete='cascade'). |
| `Command.set([ids])` | `(6, 0, [ids])` | Remplace toute la collection par la liste d'IDs fournie. |

## Champs Calculés (Computed)
```python
amount = fields.Float(compute='_compute_amount', store=True, readonly=False)

@api.depends('lines.price')
def _compute_amount(self):
    for rec in self:
        rec.amount = sum(rec.lines.mapped('price'))
```
- **compute**: Nom de la méthode.
- **store**: `True` pour persister en DB (recalcul seulement si dépendances changent).
- **inverse**: Méthode pour rendre le champ éditable (si `store=False` ou logiques complexes).
- **search**: Méthode pour permettre la recherche (si `store=False`).

## Champs Automatiques
- `id`: PK.
- `create_date`, `create_uid`: Date/User création.
- `write_date`, `write_uid`: Date/User modification.
- `display_name`: Champ calculé pour affichage (basé sur `rec_name` ou `_compute_display_name`).

## Attributs Communs
- `string`: Libellé UI.
- `help`: Tooltip.
- `readonly`: UI only (sauf si champ computed).
- `required`: UI et DB constraint (`NOT NULL`).
- `index`: `'btree'`, `'trigram'`, `True`.
- `default`: Valeur ou callable (`lambda self: ...`).
- `groups`: Restriction d'accès (xml_id des groupes).
- `company_dependent`: Valeur spécifique par société (`ir.property`).
