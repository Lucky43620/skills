# Odoo Module System (JavaScript Modules)

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/javascript_modules.html

## TL;DR

- Le module system Odoo gère l’import, l’isolation et le chargement dans les bundles.
- Les fichiers Odoo utilisent souvent l’entête `/** @odoo-module **/`.
- Les registries sont le mécanisme standard pour enregistrer widgets, services, views, etc.

## Concepts clés

- Native ES modules vs système Odoo : conventions d’import (`@web/...`, `@my_addon/...`).
- Éviter l’import side-effect non maîtrisé.

## Patterns recommandés

- Un `index.js` par feature pour regrouper les exports.
- Toujours exporter explicitement ce qui est utilisé ailleurs.

## Pièges fréquents

- Chemins d’import incorrects / alias non résolu.
- Double déclaration du même module (collision).

## Checklist

- [ ] Ajouter le fichier au bon bundle.
- [ ] Vérifier l’entête `@odoo-module` quand nécessaire.
- [ ] Tester en `debug=assets`.

## Exemples

```js
/** @odoo-module **/

import { registry } from "@web/core/registry";

registry.category("services").add("myService", {
  start(env) {
    return { hello: () => console.log("hello") };
  },
});
```

## Voir aussi

- ../registries/registry_api.md
- ../services/defining_a_service.md
