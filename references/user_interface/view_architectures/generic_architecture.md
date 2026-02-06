# Generic architecture (views)

## TL;DR

- Chaque vue est un XML `arch` stocké dans `ir.ui.view` et rendu selon un type (form/list/kanban/...).
- Les vues peuvent être composées et héritées via `xpath`.

## Concepts clés

- Couche serveur : définition XML + chargement (assets) + actions/menus.
- Couche client : rendering (OWL/webclient) + widgets + registries.

## Patterns recommandés

- Toujours définir `model` et nommer les vues de manière stable.
- Factoriser avec héritage plutôt que duplication.

## Pièges fréquents

- Confondre “vue QWeb” (reports/frontend) et “vue UI” (ir.ui.view).
