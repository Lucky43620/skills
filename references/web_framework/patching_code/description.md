# Description (Patching code)

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/patching_code.html

## TL;DR

- Le patching permet de modifier/étendre du code JS existant sans le copier.
- Approche recommandée pour “toucher” le core sans fork, mais à utiliser avec parcimonie.

## Concepts clés

- Patch nommé (id) appliqué à une cible (objet, classe, composant).
- Possibilité de retirer un patch.

## Patterns recommandés

- Patch minimal, ciblé, documenté (pour maintenance).
- Patcher `setup()` d’un composant OWL plutôt que modifier des internals.

## Pièges fréquents

- Patches qui se marchent dessus entre modules.
- Dépendance à des internals non stables (casse en upgrade).
