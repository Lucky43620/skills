# Templates Web (Odoo v19)

Ces templates sont des **snippets prêts à copier** pour le webclient Odoo v19.

## Comment les utiliser
1) Copiez le fichier dans votre module (chemin indiqué dans le snippet). 
2) Ajoutez le fichier au bundle `assets` dans `__manifest__.py`. 
3) Si le snippet contient un template QWeb (`.xml`), ajoutez-le à `web.assets_qweb`. 
4) Testez avec `?debug=assets` pour vérifier l’inclusion. 

## Fichiers clés
- `odoo_module_example.js` : exemple de module JS avec `/** @odoo-module **/`. 
- `owl_component.js` + `owl_template.xml` : composant OWL minimal. 
- `registry_add.js` / `registry_field_widget.js` : enregistrement dans les registries. 
- `service_define.js` / `service_use.js` : création + usage de services. 
- `patch_class.js` / `patch_component.js` : patching d’objets/classes. 
- `assets_in_manifest.py` : déclaration d’assets dans `__manifest__.py`. 

## Bonnes pratiques
- Toujours isoler le code backend vs frontend. 
- Garder les bundles légers (lazy loading si besoin). 
- Préférer des modules JS plutôt que du JS global. 
