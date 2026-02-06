# Report template

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/reporting.html

## TL;DR

- Un template QWeb décrit la structure du rapport (HTML/PDF).
- Il est référencé par `ir.actions.report` via `report_name`.

## Quand l’utiliser

- Pour créer un nouveau rapport QWeb.
- Pour surcharger le rendu d’un rapport existant.

## Concepts clés

- **Template QWeb** : `<template id="...">` avec `t-call` et `t-foreach`.
- **`doc` / `docs`** : enregistrements passés au template.
- **Layout** : `web.external_layout` pour l’entête/pied.

## API / Syntaxe

```xml
<!-- my_module/views/report_template.xml -->
<odoo>
  <template id="report_my_doc">
    <t t-call="web.external_layout">
      <div class="page">
        <h2><t t-esc="doc.display_name"/></h2>
        <p>Contenu...</p>
      </div>
    </t>
  </template>
</odoo>
```

## Patterns recommandés

- Utiliser `web.external_layout` pour un rendu cohérent.
- Préparer les données côté Python (peu de logique dans le template).
- Isoler les sous-templates pour la réutilisabilité.

## Anti-patterns & pièges

- Logique métier lourde dans le template.
- Oublier d’inclure le template dans les fichiers `data`.

## Debug & troubleshooting

- Tester en HTML avant de générer un PDF.
- Vérifier les variables `doc`/`docs` dans le contexte.

## Exemples complets

```python
# my_module/models/report_my_doc.py
from odoo import models

class ReportMyDoc(models.AbstractModel):
    _name = "report.my_module.report_my_doc"
    _description = "Report My Doc"

    def _get_report_values(self, docids, data=None):
        docs = self.env["res.partner"].browse(docids)
        return {"docs": docs}
```

```xml
<!-- my_module/views/report_action.xml -->
<record id="action_report_my_doc" model="ir.actions.report">
  <field name="name">Mon document</field>
  <field name="model">res.partner</field>
  <field name="report_type">qweb-pdf</field>
  <field name="report_name">my_module.report_my_doc</field>
  <field name="report_file">my_module.report_my_doc</field>
  <field name="binding_model_id" ref="model_res_partner"/>
</record>
```

## Checklist

- [ ] Template QWeb déclaré dans `data`.
- [ ] `report_name` aligné avec l’ID du template.
- [ ] Test HTML avant PDF.

## Liens officiels

- https://www.odoo.com/documentation/19.0/developer/reference/backend/reporting.html

## Voir aussi

- [QWeb reports (index)](index.md)
- [Report actions](../actions/report_actions_ir_actions_report.md)
- [Paper format](paper_format.md)
