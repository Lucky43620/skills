# Bundles (Assets)

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/assets.html

## TL;DR

- Les bundles (ex: `web.assets_backend`) regroupent JS/CSS/XML et déterminent l’ordre de chargement.
- On déclare généralement les assets dans `__manifest__.py` sous la clé `assets`.
- Debug : `?debug=assets` (non-minifié) et `?debug=tests` (tests).

## Concepts clés

- Bundles principaux : backend/frontend/common (selon besoin).
- Ordre de chargement : avant/après/remplacement possibles via directives d’assets.
- Lazy loading : charger plus tard certaines ressources.

## Patterns recommandés

- Mettre les composants UI backend dans `web.assets_backend`.
- Mettre les assets site/portal dans `web.assets_frontend` ou bundle dédié.
- Regrouper par feature : `static/src/<feature>/` avec `index.js`.

## Pièges fréquents

- Importer un module qui n’est pas dans le bundle → erreur `module not found`.
- Dépendances cycliques / ordre de chargement incorrect.
- Oublier `/** @odoo-module **/` sur fichiers concernés.

## Checklist

- [ ] Déclarer l’asset dans `__manifest__.py`.
- [ ] Vérifier la bundle cible (backend vs frontend).
- [ ] Tester en `debug=assets`.

## Exemples

```python
# __manifest__.py
{
  'assets': {
    'web.assets_backend': [
      'my_addon/static/src/**/*.js',
      'my_addon/static/src/**/*.xml',
      'my_addon/static/src/**/*.scss',
    ],
  },
}
```

## Voir aussi

- `assets/templates/web/assets_manifest_snippet.md` (à créer)
- ../javascript_modules/odoo_module_system.md
