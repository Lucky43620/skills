# Lazy Loading

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/assets.html#lazy-loading

## TL;DR

Permet de charger des assets (JS/CSS) ou bundles dynamiquement, uniquement quand nécessaire (ex: grosse librairie tierce).

## Usage

Utiliser la fonction helper `loadAssets` ou le hook `useAssets`.

### `loadAssets` (Fonction)
Retourne une Promise.

```javascript
import { loadAssets } from "@web/core/assets";

await loadAssets({
    jsLibs: ["/web/static/lib/stacktracejs/stacktrace.js"],
    cssLibs: ["/web/static/lib/some_lib.css"],
});
```

### `useAssets` (Hook)
Charge les assets automatiquement dans le `onWillStart` d'un composant.

```javascript
import { start } from "@odoo/owl";
import { useAssets } from "@web/core/assets";

class MyComponent extends Component {
    setup() {
        useAssets({
            jsLibs: ["/my_module/static/lib/heavy_lib.js"],
        });
    }
}
```
