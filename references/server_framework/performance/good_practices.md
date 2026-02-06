# Good practices (Performance)

## TL;DR

- Optimiser d’abord l’architecture ORM (domains, indexes, read_group) avant micro-optimisations Python.
- Éviter N+1 en profitant du prefetch/cache.

## Concepts clés

- Prefetch : accès à un champ fetch plusieurs records d’un coup.
- Domains sélectifs + indexes btree/trigram.
- Aggregations : read_group.

## Patterns recommandés

- Batch writes (écrire en une fois sur recordsets).
- Limiter les boucles sur gros volumes; paginer.

## Pièges fréquents

- Utiliser `sudo()` qui bypass rules → plus de données chargées → perf plus lente.

## Checklist

- [ ] Mesure (profiling) avant/après.
- [ ] Logs SQL : vérifier nombre de requêtes.
- [ ] Indices : vérifier plan de requête si besoin.
