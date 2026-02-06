# Paper Format (Reports)

Les formats de papier définissent la taille de la page (A4, Lettre) et les marges pour les rapports PDF (wkhtmltopdf).

## 1. Définition XML (`report.paperformat`)

Doit être défini dans `data/` de votre module.

```xml
<record id="paperformat_euro_landscape" model="report.paperformat">
    <field name="name">European A4 Landscape</field>
    <field name="default" eval="True" />
    <field name="format">A4</field>
    <field name="page_height">0</field>
    <field name="page_width">0</field>
    <field name="orientation">Landscape</field>
    <field name="margin_top">40</field>
    <field name="margin_bottom">23</field>
    <field name="margin_left">7</field>
    <field name="margin_right">7</field>
    <field name="header_line" eval="False" />
    <field name="header_spacing">35</field>
    <field name="dpi">90</field>
</record>
```

## 2. Assigner à un Rapport

Liez le format de papier à votre action de rapport.

```xml
<record id="action_report_saleorder" model="ir.actions.report">
    <field name="name">Quotation / Order</field>
    <field name="model">sale.order</field>
    <field name="report_type">qweb-pdf</field>
    <field name="report_name">sale.report_saleorder</field>
    <field name="paperformat_id" ref="paperformat_euro_landscape"/>
</record>
```

## 3. Points Importants
- **`header_spacing`** : Espace réservé pour le header (en mm). Si le header est coupé, augmentez cette valeur.
- **`dpi`** : Résolution. 90 est standard. Augmenter peur améliorer la netteté mais grossir le PDF.
- **`format`** : `A4`, `Letter`, ou `custom` (dans ce cas, définir height/width).
