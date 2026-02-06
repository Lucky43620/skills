# Core operations (Data Files)

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/data.html

## TL;DR

- Opérations principales : créer/mettre à jour des records et appeler des méthodes.

## Concepts clés

- `<record>` : create/update selon xmlid.
- `<field>` : assignation (inclut relations).
- `<function>` : appeler une méthode (ex: init data).

## Patterns recommandés

- Pour données qui dépendent d’autres modules : vérifier `depends` + ordre.
- Pour M2M: utiliser les commandes relationnelles ou définir via `<field eval="...">`.

## Pièges fréquents

- Écrire du Python dans eval trop complexe → illisible/fragile.

## Exemples

```xml
<record id="x_action" model="ir.actions.act_window">
  <field name="name">X</field>
  <field name="res_model">x.model</field>
  <field name="view_mode">tree,form</field>
</record>

<function model="ir.model.data" name="_update_xmlids"/>
```
