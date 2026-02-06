# Taxes (Accounting)

## TL;DR

- Page de repère pour extension/customisation.
- Objectif: savoir quel modèle hériter, où ajouter fields/methods, et quels pièges éviter.

## Concepts clés

- Identifier le modèle technique (`_name`) dans Odoo et ses champs clés.
- Surcharges/extends via `_inherit` + `super()` + règles de sécurité.

## Patterns recommandés

- Éviter de modifier le core: créer un module d’extension.
- Utiliser des hooks/registries côté web si UI spécifique.

## Pièges fréquents

- Contourner les contraintes comptables (risque d’incohérences).
- Forcer des `sudo()` en compta/paiement (risque sécurité).

## Exemples

```text
# Ajoute ici les notes spécifiques au modèle et ses relations.
```
