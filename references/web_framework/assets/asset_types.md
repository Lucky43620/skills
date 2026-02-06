# Asset types

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/assets.html

## TL;DR
- Un asset est un fichier statique (JS/SCSS/XML/QWeb/images/fonts) compilé en bundle. 
- Le type est déduit par l’extension et influence le pipeline (transpile, minify, QWeb). 
- Les templates QWeb frontend passent par `web.assets_qweb`. 
- Les assets OWL/JS modernes doivent être des modules `/** @odoo-module **/`. 
- Les `scss` permettent l’héritage et la surcharge grâce à l’ordre de compilation. 
- Les images/fonts doivent être référencés avec des chemins stables et le cache busting. 

## Quand l’utiliser
- Tu choisis la bonne extension pour activer le bon pipeline (ex: `.xml` pour QWeb). 
- Tu veux structurer les assets par type (JS, SCSS, QWeb) pour garder des bundles lisibles. 
- Tu dois diagnostiquer un rendu cassé (mauvais type, mauvais bundle). 

## Concepts clés
- **JS module** : fichier JS annoté `/** @odoo-module **/` pour le loader. 
- **QWeb template** : XML OWL/legacy chargé via `web.assets_qweb`. 
- **SCSS** : compile vers CSS avec variables/`@use`/`@import`. 
- **Static** : images, fonts, JSON, etc. livrés tels quels. 

## API / Syntaxe
### Exemple d’asset JS module
```javascript
/** @odoo-module **/
import { registry } from "@web/core/registry";

registry.category("actions").add("my_module.my_action", () => ({
  name: "My Action",
}));
```

### Exemple QWeb template
```xml
<!-- my_module/static/src/components/my_badge.xml -->
<t t-name="my_module.MyBadge" owl="1">
  <span class="o_my_badge">Badge</span>
</t>
```

### Exemple SCSS
```scss
// my_module/static/src/components/my_badge.scss
.o_my_badge {
  background: $o-brand-primary;
  color: white;
}
```

### Exemple image/font
```text
my_module/static/src/img/logo.svg
my_module/static/src/fonts/myfont.woff2
```
```scss
// my_module/static/src/scss/fonts.scss
@font-face {
  font-family: "MyFont";
  src: url("/my_module/static/src/fonts/myfont.woff2") format("woff2");
}
```

## Patterns recommandés
1) **Séparer JS/SCSS/XML dans des sous-dossiers**
```
static/src/
  components/
    my_badge.js
    my_badge.xml
    my_badge.scss
```
→ facilite la maintenance et le bundling. 

2) **Toujours annoter les modules JS**
```javascript
/** @odoo-module **/
```
→ évite les erreurs de chargement du loader. 

3) **Ranger les assets par contexte (backend/frontend)**
```
static/src/backend/...
static/src/website/...
```
→ évite le code chargé au mauvais endroit. 

## Anti-patterns & pièges
- **Mettre un template QWeb dans `web.assets_backend`** → non chargé par le moteur QWeb frontend. 
- **Oublier `owl="1"`** → template non traité par OWL. 
- **Utiliser du JS global** → collisions et dépendances implicites. 
- **Importer une image sans chemin stable** → 404 en production. 

## Debug & troubleshooting
- `?debug=assets` pour voir les fichiers compilés. 
- Vérifie l’extension et la présence dans le bon bundle. 
- Inspecte le DOM pour confirmer que le template QWeb est bien chargé. 
- Vérifie les URLs statiques (`/my_module/static/...`) pour les 404. 

## Exemples complets
### Exemple — Widget complet
```
my_module/
  static/src/widgets/status_badge.js
  static/src/widgets/status_badge.xml
  static/src/widgets/status_badge.scss
```
```javascript
/** @odoo-module **/
import { Component } from "@odoo/owl";

export class StatusBadge extends Component {}
StatusBadge.template = "my_module.StatusBadge";
```

## Checklist
- [ ] Extension correcte (JS/SCSS/XML). 
- [ ] Module JS annoté `@odoo-module`. 
- [ ] Template QWeb dans `web.assets_qweb`. 
- [ ] Aucun asset hors contexte (backend vs frontend). 

## Liens officiels
- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/assets.html

## Voir aussi
- [Assets](index.md)
- [Bundles](bundles.md)
- [Lazy loading](lazy_loading.md)
- [QWeb Templates](../qweb_templates/index.md)
