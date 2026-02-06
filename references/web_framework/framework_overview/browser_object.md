# Browser Object

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html#browser-object

## TL;DR

Odoo encapsule les APIs natives du navigateur (`window`, `localStorage`, `setTimeout`) dans un objet `browser` pour faciliter le **Mocking** lors des tests.

## Pourquoi ?
Si vous utilisez `window.setTimeout` directement dans votre code, vos tests unitaires devront attendre le délai réel, ou vous devrez monkey-patcher `window` (risqué).
Avec `browser.setTimeout`, un test peut simplement remplacer `browser.setTimeout` par une fonction immédiate sans affecter l'environnement global.

## Usage

```javascript
import { browser } from "@web/core/browser/browser";

// Au lieu de setTimeout(fn, 1000)
browser.setTimeout(() => {
    console.log("Delayed");
}, 1000);

// Au lieu de localStorage.setItem
browser.localStorage.setItem("key", "value");
```

## APIs exposées
- `addEventListener`, `removeEventListener`
- `setTimeout`, `clearTimeout`, `setInterval`, `clearInterval`
- `fetch`, `XMLHttpRequest`
- `localStorage`, `sessionStorage`
- `location`, `history`, `navigator`
- `console`
- `Date` (utile pour mocker le temps!)
