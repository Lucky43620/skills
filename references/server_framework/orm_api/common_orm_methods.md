# Common ORM Methods

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/backend/orm.html#common-orm-methods

## CRUD

### `create(vals_list)`
Crée des enregistrements.
- **vals_list**: Liste de dictionnaires (ou un seul dictionnaire).
- **Retourne**: Le recordset créé.

```python
records = self.env['my.model'].create([
    {'name': 'A', 'value': 10},
    {'name': 'B', 'value': 20},
])
```

### `write(vals)`
Met à jour tous les enregistrements du recordset courant.
- **vals**: Dictionnaire de valeurs.
- **Retourne**: `True`.

```python
records.write({'active': False})
```

### `unlink()`
Supprime les enregistrements du recordset courant.
- **Retourne**: `True`.

```python
records.unlink()
```

### `copy(default=None)`
Duplique l'enregistrement (singleton).
- **default**: Dictionnaire de valeurs pour surcharger la copie.
- **Retourne**: Le nouvel enregistrement.

## Lecture & Recherche

### `search(domain, offset=0, limit=None, order=None)`
Recherche des enregistrements.
- **domain**: Liste de tuples (ex: `[('field', '=', 'value')]`).
- **Retourne**: Recordset.

```python
partners = self.env['res.partner'].search([('is_company', '=', True)], limit=10)
```

### `search_count(domain)`
Retourne le nombre d'enregistrements correspondant au domaine.

### `browse(ids)`
Instancie un recordset à partir d'une liste d'IDs.
Ne fait pas de requête DB immédiatement (lazy).

```python
partners = self.env['res.partner'].browse([1, 2, 3])
```

### `read(fields=None)`
Retourne une liste de dictionnaires (bas niveau, pour UI/RPC).
- **fields**: Liste de noms de champs à lire.

### `read_group(domain, fields, groupby, ...)`
Lecture agrégée (SQL GROUP BY). Utilisé pour les vues Graph, Pivot, Kanban.

## Méthodes Utilitaires

### `filtered(func_or_field)`
Filtre le recordset (en mémoire Python, pas en DB).
- `records.filtered(lambda r: r.amount > 100)`
- `records.filtered('active')`

### `mapped(func_or_field)`
Transforme le recordset.
- `records.mapped('name')` -> Retourne liste des noms.
- `records.mapped('line_ids')` -> Retourne recordset fusionné des lignes.

### `sorted(key=None, reverse=False)`
Trie le recordset.
