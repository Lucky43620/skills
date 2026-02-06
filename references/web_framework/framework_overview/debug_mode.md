# Debug Mode

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html#debug-mode

## TL;DR

Le mode debug active des outils développeur et affiche plus d'infos (noms techniques des champs). Il est stocké dans l'URL (`?debug=1` ou `?debug=assets`).

## Accès JS

Accessible via `env.debug` (string).
- `""` (vide) : Inactif.
- `"1"`, `"assets"`, `"tests"`, `"assets,tests"` : Actif.

```javascript
if (this.env.debug) {
    console.log("Debug mode is on");
}
```

## Modes spécifiques

### Debug Assets (`debug=assets`)
- Désactive la minification des assets (JS/CSS).
- Génère les Source Maps.
- Indispensable pour déboguer le code JS dans le navigateur.

### Debug Tests (`debug=tests`)
- Active les outils liés aux tests (ex: tours).

## Visibilité XML

Pour afficher un champ ou bouton *uniquement* en mode debug, utiliser le groupe technique "No One" (si possible) ou vérifier le contexte (mais `base.group_no_one` est la convention).

```xml
<field name="fname" groups="base.group_no_one"/>
```
