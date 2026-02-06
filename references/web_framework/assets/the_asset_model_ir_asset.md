# The asset model (ir.asset)

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/assets.html

## TL;DR
- `ir.asset` permet d’ajouter, retirer ou remplacer un asset via XML. 
- Idéal pour patcher un bundle standard sans modifier le module source. 
- Supporte `add`, `remove`, `replace`, `before`, `after`. 
- L’ordre d’exécution des records influence la composition finale du bundle. 
- Utilise des chemins absolus (`/web/static/...`). 

## Quand l’utiliser
- Tu dois enlever un asset standard (legacy CSS, JS). 
- Tu veux injecter un override conditionnel sans toucher au module d’origine. 
- Tu développes un module d’intégration qui doit rester isolé. 

## Concepts clés
- **Bundle** : champ `bundle` de `ir.asset` (ex: `web.assets_backend`). 
- **Directive** : `add`, `remove`, `replace`, `before`, `after`. 
- **Path** : chemin de l’asset cible (à retirer/remplacer). 

## API / Syntaxe
### Retirer un asset
```xml
<record id="my_module_remove_asset" model="ir.asset">
  <field name="name">my_module remove asset</field>
  <field name="bundle">web.assets_backend</field>
  <field name="directive">remove</field>
  <field name="path">/web/static/src/scss/legacy.scss</field>
</record>
```

### Remplacer un asset
```xml
<record id="my_module_replace_asset" model="ir.asset">
  <field name="name">my_module replace asset</field>
  <field name="bundle">web.assets_backend</field>
  <field name="directive">replace</field>
  <field name="path">/web/static/src/js/core/browser.js</field>
  <field name="content">/my_module/static/src/override/browser.js</field>
</record>
```

### Injecter avant/après
```xml
<record id="my_module_after_asset" model="ir.asset">
  <field name="name">my_module after asset</field>
  <field name="bundle">web.assets_backend</field>
  <field name="directive">after</field>
  <field name="path">/web/static/src/webclient/webclient.js</field>
  <field name="content">/my_module/static/src/patch/webclient_patch.js</field>
</record>
```

## Patterns recommandés
1) **Patcher sans fork**
→ `ir.asset` pour maintenir la compatibilité avec les updates. 

2) **Centraliser les overrides**
```
my_module/views/assets.xml
```
→ évite la dispersion des patches. 

3) **Documenter chaque override**
```xml
<field name="name">why: fix conflict with module X</field>
```
→ utile en maintenance. 

## Anti-patterns & pièges
- **Path relatif** → l’asset n’est pas trouvé. 
- **`replace` sans `content`** → bundle cassé. 
- **Multiples overrides contradictoires** → ordre non déterministe. 

## Debug & troubleshooting
- `?debug=assets` pour inspecter le bundle final. 
- Vérifie la présence du record `ir.asset` dans la base (mode dev). 
- Cherche les collisions d’override dans d’autres modules. 

## Exemples complets
### Exemple — Retirer une feuille de style legacy
```
my_module/views/assets.xml
```
```xml
<odoo>
  <record id="my_module_remove_legacy" model="ir.asset">
    <field name="name">my_module remove legacy scss</field>
    <field name="bundle">web.assets_backend</field>
    <field name="directive">remove</field>
    <field name="path">/web/static/src/scss/legacy.scss</field>
  </record>
</odoo>
```

## Checklist
- [ ] Bundle correct (backend/frontend/tests). 
- [ ] Path absolu valide. 
- [ ] Directive adaptée (`remove`/`replace`/`before`/`after`). 
- [ ] Testé en `?debug=assets`. 

## Liens officiels
- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/assets.html

## Voir aussi
- [Assets](index.md)
- [Asset types](asset_types.md)
- [Patching code](../patching_code/index.md)
