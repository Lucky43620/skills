# Recordsets (ORM API)

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/orm.html

## TL;DR

- Un recordset = collection ordonnée de records d’un modèle (peut être vide, 1 ou N).
- `self` est presque toujours un recordset (multi) : coder en conséquence.
- Le cache/prefetch réduit les requêtes; éviter les patterns N+1.

## Concepts clés

- Recordset vide (`self` falsy) vs singleton vs multi.
- Opérations classiques: `mapped`, `filtered`, `sorted`, `exists`, `sudo`, `with_context`, `with_company`.
- `browse(ids)` ne fait pas de query immédiate; `search(domain)` oui.

## Patterns recommandés

- Boucler `for rec in self:` quand on écrit sur des champs.
- Utiliser `ensure_one()` quand on accède à un champ supposé unique.
- Regrouper les reads (prefetch) et éviter `search` dans des boucles.

## Pièges fréquents

- Appeler une méthode qui suppose 1 record sur un recordset multi (bugs silencieux ou erreurs).
- Faire `for rec in self: rec.other_id.name` sans anticiper prefetch (N+1 sur relations complexes).
- Confondre recordset et liste d’ids (ex: `ids` vs `mapped('id')`).

## Checklist

- [ ] Cette méthode fonctionne-t-elle si `self` contient plusieurs records ?
- [ ] Y a-t-il des searches dans une boucle ?
- [ ] Peut-on remplacer par `read_group`, `search_read`, `search_fetch` (si dispo) ?

## Exemples

```python
# mapped / filtered / sorted
partners = self.mapped('partner_id').filtered(lambda p: p.active)
partners = partners.sorted(key=lambda p: p.name or "")
```

```python
# ensure_one
self.ensure_one()
return self.name
```

```python
# with_context / sudo
records = self.with_context(active_test=False).sudo()
```
