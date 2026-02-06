# Odoo Module System (JS)

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/javascript_modules.html

Odoo v19 utilise presque exclusivement les **Modules Natifs ES6**.

## 1. Définition standard (Native Modules)
Tout fichier JS qui commence par le commentaire magique `/** @odoo-module **/` est traité comme un module Odoo.

**Chemin :** `my_module/static/src/my_file.js`
```javascript
/** @odoo-module **/

// Imports depuis d'autres modules Odoo (via alias)
import { registry } from "@web/core/registry";
import { MyComponent } from "@my_module/components/my_component";

// Export standard
export class MyService {
    // ...
}
```

## 2. Système d'Alias
Odoo mappe automatiquement les fichiers statiques des addons.
Format : `@nom_addon/chemin/vers/fichier`

- Fichier réel : `addons/account/static/src/components/account_move.js`
- Import : `import { ... } from "@account/components/account_move";`

**Attention :** N'ajoutez PAS `.js` à la fin de l'import aliasé.

## 3. Debugging
Contrairement aux bundles minifiés, Odoo charge les modules natifs individuellement en mode debug.

- **Activer le debug** : Ajoutez `?debug=assets` dans l'URL.
- **Trouver son fichier** : Dans les DevTools du navigateur (F12) -> Sources -> dossier `odoo` ou `custom` -> `nom_addon` -> `static/src/...`.
- **Breakpoints** : Vous pouvez mettre des `debugger;` directement dans votre code.

## 4. Legacy `odoo.define` (Déprécié)
À utiliser UNIQUEMENT si vous migrez du très vieux code ou si vous interagissez avec des libs non-modulaires.

```javascript
odoo.define('my_module.MyWidget', function (require) {
    "use strict";
    var Widget = require('web.Widget');
    // ...
    return MyWidget;
});
```

## 5. Bonnes Pratiques
- **Toujours** mettre `/** @odoo-module **/` en première ligne.
- **Toujours** utiliser des imports explicites au début du fichier.
- Évitez les "side-effects" (code qui s'exécute à l'import) sauf pour l'enregistrement dans la `registry`.
