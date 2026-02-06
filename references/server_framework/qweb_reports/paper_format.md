# Paper format

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/reporting.html

## TL;DR

- Le `paperformat` contrôle la taille, marges et orientation des rapports PDF.
- Il peut être assigné à une action de rapport.

## Quand l’utiliser

- Pour adapter un rapport à un format légal (A4, Letter).
- Pour ajuster des marges ou l’orientation (portrait/paysage).

## Concepts clés

- **`report.paperformat`** : modèle qui définit le format.
- **Action de rapport** : champ `paperformat_id`.

## API / Syntaxe

```xml
<!-- my_module/views/paperformat.xml -->
<record id="paperformat_my_doc" model="report.paperformat">
  <field name="name">My Doc A4</field>
  <field name="format">A4</field>
  <field name="orientation">Portrait</field>
  <field name="margin_top">20</field>
  <field name="margin_bottom">20</field>
</record>
```

```xml
<!-- my_module/views/report_action.xml -->
<record id="action_report_my_doc" model="ir.actions.report">
  <field name="name">Mon document</field>
  <field name="model">res.partner</field>
  <field name="report_type">qweb-pdf</field>
  <field name="report_name">my_module.report_my_doc</field>
  <field name="paperformat_id" ref="paperformat_my_doc"/>
</record>
```

## Patterns recommandés

- Définir un format par rapport si nécessaire.
- Réutiliser un `paperformat` commun pour plusieurs rapports.

## Anti-patterns & pièges

- Marges trop faibles → contenu coupé.
- Format non supporté par le moteur PDF.

## Debug & troubleshooting

- Tester en HTML pour vérifier le rendu avant PDF.
- Ajuster les marges progressivement.

## Exemples complets

```text
my_module/views/paperformat.xml
my_module/views/report_action.xml
```

## Checklist

- [ ] `paperformat` défini et chargé dans `data`.
- [ ] Action de rapport liée via `paperformat_id`.
- [ ] PDF validé sur plusieurs imprimantes.

## Liens officiels

- https://www.odoo.com/documentation/19.0/developer/reference/backend/reporting.html

## Voir aussi

- [Report template](report_template.md)
- [QWeb reports (index)](index.md)
- [Report actions](../actions/report_actions_ir_actions_report.md)
