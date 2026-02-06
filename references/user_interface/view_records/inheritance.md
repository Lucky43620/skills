# Inheritance (View records)

## TL;DR

- Hériter d’une vue via `inherit_id` + `xpath` pour modifier une vue existante sans duplication.
- Approche recommandée pour maintenir la compatibilité upgrades.

## Concepts clés

- Record `ir.ui.view` avec `inherit_id` pointant vers la vue parent.
- `xpath` pour insérer/remplacer/attribuer : positions `inside`, `before`, `after`, `replace`, `attributes`.

## Patterns recommandés

- XPaths courts et robustes (cibler par `name`/`position` plutôt que par index).
- Éviter `replace` de blocs énormes; préférer insertions ciblées.

## Pièges fréquents

- XPath qui casse si la vue parent change (upgrade).
- Héritages multiples contradictoires (ordre).

## Exemples

```xml
<record id="view_res_partner_form_inherit_my" model="ir.ui.view">
  <field name="name">res.partner.form.inherit.my</field>
  <field name="model">res.partner</field>
  <field name="inherit_id" ref="base.view_partner_form"/>
  <field name="arch" type="xml">
    <xpath expr="//field[@name='name']" position="after">
      <field name="x_code"/>
    </xpath>
  </field>
</record>
```
