# Installation

## TL;DR

- Résumé + structure type + bonnes pratiques.

## Concepts clés

- Phases d’upgrade, hooks, data migrations, compat.

## Patterns recommandés

- Script idempotent, logs, tests.

## Pièges fréquents

- Exécuter du code non idempotent, casser contraintes.

## Exemples

```python
# Exemple de squelette d'upgrade
def migrate(cr, version):
    pass
```
