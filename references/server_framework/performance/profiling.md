# Profiling

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/performance.html

## TL;DR

- Le profiling aide à identifier les goulots d’étranglement (SQL, Python, QWeb).
- Utiliser des logs ciblés et des outils de profiling pour mesurer avant d’optimiser.

## Quand l’utiliser

- Quand une action ou un écran est lent.
- Quand une requête ORM génère trop de SQL.

## Concepts clés

- **Profiling applicatif** : mesurer le temps côté Python/ORM.
- **Profiling SQL** : analyser les requêtes et index.
- **Profiling frontend** : temps de rendu côté client.

## API / Syntaxe

- Activer des logs de requêtes SQL :
```text
--db-filter=... --log-level=debug_sql
```

- Utiliser un profiler Python externe (ex: `cProfile`) dans un environnement de dev.

## Patterns recommandés

- Mesurer avant/après chaque optimisation.
- Ajouter des index sur les champs filtrés fréquemment.
- Réduire les `search_read` en limitant les champs.

## Anti-patterns & pièges

- Optimiser sans mesure (risque de régression).
- Ajouter des index inutiles (écriture plus lente).

## Debug & troubleshooting

- Inspecter les requêtes SQL générées par l’ORM.
- Vérifier les appels répétés dans les traces.

## Exemples complets

```python
# my_module/models/reporting.py
from odoo import models

class Reporting(models.AbstractModel):
    _name = "my_module.reporting"

    def get_stats(self):
        self.env.cr.execute("""
            SELECT partner_id, count(*)
            FROM sale_order
            GROUP BY partner_id
        """)
        return self.env.cr.fetchall()
```

## Checklist

- [ ] Mesures réalisées avant optimisation.
- [ ] Requêtes SQL inspectées.
- [ ] Index ajoutés uniquement si nécessaires.

## Liens officiels

- https://www.odoo.com/documentation/19.0/developer/reference/backend/performance.html

## Voir aussi

- [Performance (index)](index.md)
- [Good practices](good_practices.md)
- [ORM API](../orm_api/index.md)
