# Patching code

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/patching_code.html

Rubrique **Patching code** (Web framework) : frontend Odoo (JS/Owl) + architecture webclient.

## Sous-rubriques

- [Description](description.md)
- [Patching a simple object](patching_a_simple_object.md)
- [Patching a javascript class](patching_a_javascript_class.md)
- [Patching a component](patching_a_component.md)
- [Removing a patch](removing_a_patch.md)
- [Applying the same patch to multiple objects](applying_the_same_patch_to_multiple_objects.md)

## Checklist rapide

- Identifier le besoin exact (API / XML / UI / perf / sécurité).
- Repérer les fichiers Odoo concernés (Python, XML, CSV, JS).
- Appliquer un pattern de référence (snippets).
- Vérifier tests + debug.
