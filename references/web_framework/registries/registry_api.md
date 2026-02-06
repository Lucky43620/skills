# Registry API (Registries)

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/registries.html

## TL;DR

- Les registries sont le mécanisme d’extension standard du webclient Odoo.
- On ajoute des entrées dans une catégorie (views, fields, services, systray, …).

## Concepts clés

- Import : `import { registry } from '@web/core/registry'`.
- Catégories : `registry.category('<name>')`.
- Chaque catégorie a ses conventions (shape de l’objet).

## Patterns recommandés

- Choisir la bonne catégorie (fields vs views vs services).
- Noms/keys stables et prefixés (évite collision).

## Pièges fréquents

- Enregistrer dans la mauvaise catégorie → runtime errors difficiles à lire.
- Oublier d’ajouter le fichier au bundle → pas d’enregistrement.

## Exemples

```js
/** @odoo-module **/
import { registry } from "@web/core/registry";

registry.category("systray").add("my_addon.systray", {
  Component: MySystray,
}, { sequence: 20 });
```

## Voir aussi

- ../services/defining_a_service.md
- ../owl_components/using_owl_components.md
