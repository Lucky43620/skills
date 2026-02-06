# Assets

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/assets.html

## TL;DR
- Les `assets` sont la chaîne de build qui assemble JS/CSS/XML/QWeb du webclient. 
- Tout se déclare via `__manifest__.py` (clé `assets`) ou via `ir.asset` pour surcharger à chaud. 
- Les bundles standards (`web.assets_backend`, `web.assets_frontend`, `web.assets_common`, etc.) structurent le chargement. 
- La priorité se gère par l’ordre des fichiers et les opérateurs `before/after/replace`. 
- Utilise `?debug=assets` pour diagnostiquer le contenu d’un bundle et le cache. 
- Évite de tout mettre dans `web.assets_backend` : charge seulement ce dont tu as besoin. 
- Les templates QWeb frontend (`.xml`) doivent être dans un bundle qui inclut `web.assets_qweb`. 
- Les dépendances inter-modules sont déclarées dans `depends` du manifest, pas dans les bundles. 
- Préfère les modules JS (`/** @odoo-module **/`) et OWL à du JS global. 

## Quand l’utiliser
- Tu ajoutes du JS/SCSS/QWeb côté webclient (backend ou frontend). 
- Tu veux étendre des vues via un widget JS, un service ou un patch. 
- Tu dois optimiser le temps de chargement (lazy loading, scission de bundles). 
- Tu dois corriger/retirer un asset standard sans forker le module d’origine. 

## Concepts clés
- **Bundle** : groupe logique de fichiers chargés ensemble (backend, frontend, tests). 
- **Ordre de compilation** : détermine la surcharge CSS/JS (dernier gagne). 
- **Types d’assets** : `js`, `scss`, `xml`, `css`, `png`, `woff2`, etc. 
- **`ir.asset`** : modèle serveur pour injecter/retirer des assets via XML (override). 
- **Debug assets** : mode dégroupé + chemins source pour inspecter les dépendances. 

## API / Syntaxe
### Déclaration dans le manifest
```python
# my_module/__manifest__.py
{
    "name": "My Module",
    "depends": ["web"],
    "assets": {
        "web.assets_backend": [
            "my_module/static/src/**/*.js",
            "my_module/static/src/**/*.scss",
        ],
        "web.assets_qweb": [
            "my_module/static/src/**/*.xml",
        ],
        "web.assets_frontend": [
            "my_module/static/src/website/**/*.js",
        ],
    },
}
```

### Override avec `ir.asset`
```xml
<!-- my_module/views/assets.xml -->
<odoo>
  <record id="my_module_remove_asset" model="ir.asset">
    <field name="name">my_module remove asset</field>
    <field name="bundle">web.assets_backend</field>
    <field name="directive">remove</field>
    <field name="path">/web/static/src/scss/legacy.scss</field>
  </record>
</odoo>
```

## Patterns recommandés
1) **Bundle minimal par feature**
```text
# my_module/static/src/feature/
- feature.js
- feature.scss
- feature.xml
```
→ évite d’alourdir le bundle principal. 

2) **Découper backend vs frontend**
```python
"assets": {
  "web.assets_backend": ["my_module/static/src/backend/**/*"],
  "web.assets_frontend": ["my_module/static/src/website/**/*"],
}
```
→ charge uniquement là où nécessaire. 

3) **Utiliser `before/after/replace` pour patcher proprement**
```python
"web.assets_backend": [
  ("after", "web/static/src/webclient/webclient.js", "my_module/static/src/webclient_patch.js"),
]
```
→ garantit la dépendance d’ordre. 

4) **Assets QWeb séparés**
```python
"web.assets_qweb": ["my_module/static/src/**/*.xml"]
```
→ évite que les templates ne soient oubliés. 

## Anti-patterns & pièges
- **Tout mettre dans `web.assets_backend`** → ralentit toutes les pages backend. 
- **Oublier `web.assets_qweb`** → templates OWL non trouvés. 
- **Du JS global sans `@odoo-module`** → collisions de scope et ordre fragile. 
- **Patcher un asset standard sans `ir.asset`** → difficile à désactiver/maintenir. 

## Debug & troubleshooting
- Ouvre le webclient avec `?debug=assets` pour voir les fichiers exacts d’un bundle. 
- Utilise `?debug=tests` pour charger les assets de test. 
- Vérifie les chemins (`/module/static/src/...`) et l’ordre de surcharge. 
- Inspecte `ir.asset` si un fichier “disparaît”. 

## Exemples complets
### Exemple 1 — Ajout d’un composant OWL + style
```
my_module/
  __manifest__.py
  static/src/components/kanban_badge.js
  static/src/components/kanban_badge.xml
  static/src/components/kanban_badge.scss
```
```python
# my_module/__manifest__.py
"assets": {
  "web.assets_backend": [
    "my_module/static/src/components/kanban_badge.js",
    "my_module/static/src/components/kanban_badge.scss",
  ],
  "web.assets_qweb": [
    "my_module/static/src/components/kanban_badge.xml",
  ],
}
```

### Exemple 2 — Override d’un asset standard
```
my_module/views/assets.xml
```
```xml
<odoo>
  <record id="my_module_replace_asset" model="ir.asset">
    <field name="name">my_module replace asset</field>
    <field name="bundle">web.assets_backend</field>
    <field name="directive">replace</field>
    <field name="path">/web/static/src/js/core/browser.js</field>
    <field name="content">/my_module/static/src/override/browser.js</field>
  </record>
</odoo>
```

## Checklist
- [ ] Le bundle ciblé est correct (backend/frontend/tests). 
- [ ] Les templates `.xml` sont dans `web.assets_qweb`. 
- [ ] L’ordre des fichiers garantit la surcharge voulue. 
- [ ] Testé avec `?debug=assets`. 
- [ ] Aucun asset inutile chargé globalement. 

## Liens officiels
- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/assets.html

## Voir aussi
- [Asset types](asset_types.md)
- [Lazy loading](lazy_loading.md)
- [The asset model (ir.asset)](the_asset_model_ir_asset.md)
- [Odoo Module System](../javascript_modules/odoo_module_system.md)
- [Patching code](../patching_code/index.md)
