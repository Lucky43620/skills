# Common ORM methods (ORM API)

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/orm.html

## TL;DR

- CRUD : `create`, `write`, `unlink`, `copy`, `read`/`read_group`.
- Recherche : `search`, `search_count`, `name_search`.
- Utilitaires recordset : `mapped`, `filtered`, `sorted`, `exists`.

## Concepts clés

- Méthodes de navigation : `browse`, `search`, `search_read`.
- Compute/store/inverse : impacts sur write, recompute, domains, perf.
- Cache/prefetch : accès à un champ peut déclencher un prefetch sur un ensemble.

## Patterns recommandés

- Limiter `search` dans les boucles ; préférer un `search` unique, puis `mapped`.
- Utiliser `read_group` pour agrégations plutôt qu’itérer en Python.
- Pour perf : mesurer (profiling) avant optimisation.

## Pièges fréquents

- Ne pas respecter les conventions d’argument (domain vs args selon versions).
- Appeler `unlink()` sans vérifier les droits / ondelete / contraintes.

## Exemples

```python
# search + write
recs = self.search([('state', '=', 'draft')])
recs.write({'state': 'done'})
```

```python
# read_group (agrégation)
data = self.read_group([('active','=',True)], ['company_id'], ['company_id'])
```

## Voir aussi

- recordsets.md
- ../performance/good_practices.md
