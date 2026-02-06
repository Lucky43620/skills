# Report Actions (ir.actions.report)

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/actions.html

## TL;DR

- `ir.actions.report` déclenche un rapport (souvent QWeb PDF ou HTML).
- L’action est liée à un modèle et à un template QWeb.

## Quand l’utiliser

- Pour générer des documents (factures, bons de livraison, attestations).
- Pour exposer un bouton “Imprimer” depuis un modèle.

## Concepts clés

- **`report_name`** : nom du template QWeb.
- **`model`** : modèle métier du rapport.
- **`report_type`** : HTML/PDF selon le rendu souhaité.

## API / Syntaxe

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

## Patterns recommandés

- Déclarer un template QWeb dédié dans `static/src/xml` ou `views`.
- Utiliser un `paperformat` spécifique si besoin de marges/format.
- Lier l’action au modèle pour l’ajouter à la barre d’impression.

## Anti-patterns & pièges

- `report_name` non aligné avec le template QWeb → rapport vide.
- Oublier le `binding_model_id` → action non visible dans le menu d’impression.

## Debug & troubleshooting

- Tester le rapport en HTML avant PDF pour diagnostiquer le template.
- Vérifier la présence du template QWeb en mode debug.

## Exemples complets

```xml
<!-- my_module/views/report_template.xml -->
<odoo>
  <template id="report_my_doc">
    <t t-call="web.external_layout">
      <div class="page">
        <h2>Document</h2>
        <p><t t-esc="doc.name"/></p>
      </div>
    </t>
  </template>
</odoo>
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

- [ ] Template QWeb présent et référencé.
- [ ] `model` et `binding_model_id` cohérents.
- [ ] Test HTML puis PDF.

## Liens officiels

- https://www.odoo.com/documentation/19.0/developer/reference/backend/actions.html

## Voir aussi

- [QWeb reports](../qweb_reports/index.md)
- [Report template](../qweb_reports/report_template.md)
- [Paper format](../qweb_reports/paper_format.md)
- [Actions (index)](index.md)
