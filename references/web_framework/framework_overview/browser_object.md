# Browser object

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html

## TL;DR

- Le navigateur expose des APIs (localStorage, history, fetch) à utiliser avec prudence.
- Odoo privilégie des abstractions (`services`) pour la navigation et les RPC.

## Quand l’utiliser

- Pour des besoins spécifiques (Storage local, Clipboard, History).
- Quand aucun service Odoo ne couvre le besoin.

## Concepts clés

- `window`, `document` et APIs DOM.
- Limiter l’accès direct pour éviter les conflits avec le web client.

## API / Syntaxe

- Navigation : privilégier `env.services.action` ou `router` Odoo.
- Storage : `localStorage.getItem(...)` en fallback.

## Patterns recommandés

- Encapsuler l’usage du navigateur dans un service dédié.
- Vérifier la disponibilité (`if ("clipboard" in navigator)`).

## Anti-patterns & pièges

- Manipuler le DOM hors cycle OWL.
- Accéder à `window` dans des modules exécutés côté serveur (SSR tests).

## Debug & troubleshooting

- Tester les fonctionnalités dans un navigateur compatible.
- Ajouter des guards pour éviter les erreurs SSR.

## Exemples complets

```javascript
// my_module/static/src/js/browser_storage.js
/** @odoo-module **/

export function saveDraft(key, value) {
    if (window?.localStorage) {
        window.localStorage.setItem(key, value);
    }
}
```

## Checklist

- [ ] L’accès au navigateur est encapsulé.
- [ ] Des guards de compatibilité sont présents.
- [ ] Pas de manipulation DOM directe hors OWL.

## Liens officiels

- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html

## Voir aussi

- [Services](../services.md)
- [Hooks](../hooks.md)
- [Error handling](../error_handling.md)
