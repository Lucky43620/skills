# Lazy loading

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/assets.html

## TL;DR
- Le lazy loading charge du JS uniquement quand la feature est utilisée. 
- Idéal pour les écrans rarement consultés (reporting, assistants). 
- Utilise des `import()` dynamiques et des registries. 
- Le bundle principal reste léger, les chunks sont chargés à la demande. 
- Teste en `?debug=assets` pour vérifier les dépendances. 

## Quand l’utiliser
- Tu ajoutes une feature rarement déclenchée par l’utilisateur. 
- Tu veux réduire le temps de chargement initial du backend. 
- Tu introduis des lib lourdes (charting, éditeur). 

## Concepts clés
- **Chunk** : portion de code chargée via `import()` à l’exécution. 
- **Registry lazy** : enregistre une action/commande uniquement quand appelée. 
- **Dynamic import** : `await import("...path...")` retourne un module. 

## API / Syntaxe
### Import dynamique dans une action client
```javascript
/** @odoo-module **/
import { registry } from "@web/core/registry";

registry.category("actions").add("my_module.lazy_action", async (env, action) => {
  const { LazyAction } = await import("@my_module/lazy_action");
  return new LazyAction(env, action);
});
```

### Charger un composant à la demande
```javascript
/** @odoo-module **/
export async function loadMyWidget() {
  const { MyWidget } = await import("@my_module/widgets/my_widget");
  return MyWidget;
}
```

## Patterns recommandés
1) **Isoler les features lourdes**
```
static/src/lazy/
  my_heavy_action.js
  my_heavy_action.xml
```
→ bundle séparé via `import()` pour éviter le coût initial. 

2) **Registry + import dynamique**
```javascript
registry.category("actions").add("my_module.report", async () => {
  const { ReportAction } = await import("@my_module/report_action");
  return ReportAction;
});
```
→ l’action n’est chargée que lorsqu’elle est appelée. 

3) **Préchargement conditionnel**
```javascript
if (env.services.user.hasGroup("my_module.group_power")) {
  import("@my_module/power_panel");
}
```
→ prépare le code pour les profils qui en ont besoin. 

## Anti-patterns & pièges
- **Lazy loading de tout** → complexité inutile et UX dégradée. 
- **Importer un module sans déclarer ses assets** → 404 en production. 
- **Dépendances cycliques** → erreurs de chargement. 

## Debug & troubleshooting
- `?debug=assets` pour voir les fichiers et les chunks. 
- Vérifie la présence des fichiers dans le bundle source. 
- Surveille la console pour erreurs `Uncaught (in promise)` liées à `import()`. 

## Exemples complets
### Exemple — Action client lazy
```
my_module/
  static/src/lazy/my_action.js
  static/src/lazy/my_action.xml
```
```javascript
/** @odoo-module **/
import { registry } from "@web/core/registry";

registry.category("actions").add("my_module.lazy", async () => {
  const { MyLazyAction } = await import("@my_module/lazy/my_action");
  return MyLazyAction;
});
```

## Checklist
- [ ] La feature est réellement rare/optionnelle. 
- [ ] Les chemins `import()` pointent vers des modules existants. 
- [ ] Les assets nécessaires sont déclarés dans le manifest. 
- [ ] Testé en `?debug=assets`. 

## Liens officiels
- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/assets.html

## Voir aussi
- [Assets](index.md)
- [Asset types](asset_types.md)
- [Javascript Modules](../javascript_modules/index.md)
- [Registries](../registries/index.md)
