# Debug mode

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html

## TL;DR

- Le mode debug expose les assets, les vues et les actions pour diagnostiquer. 
- Il facilite l’inspection des registries et des templates chargés. 

## Quand l’utiliser

- Quand un module JS n’est pas chargé.
- Pour inspecter les bundles ou recharger en mode non minifié.

## Concepts clés

- `?debug=assets`: charge les fichiers source séparés.
- `?debug=1`: active la barre debug et l’inspection.

## API / Syntaxe

- Accès : ajouter `?debug=assets` à l’URL.
- Côté JS : activer des logs conditionnels.

## Patterns recommandés

- Utiliser `debug=assets` lors du développement front.
- Garder des logs `console.debug` derrière un flag.

## Anti-patterns & pièges

- Laisser des logs bruyants en production.
- Dépendre d’un comportement de debug pour des features.

## Debug & troubleshooting

- Vérifier que le bundle contient le fichier souhaité.
- Inspecter les templates QWeb chargés.

## Exemples complets

```text
https://odoo.local/web?debug=assets
```

```javascript
// my_module/static/src/js/logger.js
/** @odoo-module **/

const isDebug = new URLSearchParams(window.location.search).get("debug");
if (isDebug) {
    console.debug("Mode debug actif");
}
```

## Checklist

- [ ] URL en `debug=assets` pour diagnostiquer.
- [ ] Les bundles sont inspectés.
- [ ] Pas de logs restants en prod.

## Liens officiels

- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html

## Voir aussi

- [Assets](../assets.md)
- [Error handling](../error_handling.md)
- [Modules JavaScript](../javascript_modules.md)
