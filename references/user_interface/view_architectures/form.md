# Form view (architecture XML)

## TL;DR

- La vue form décrit l’édition d’un record (group, notebook, sheet, chatter…).
- L’héritage se fait via `inherit_id` + `xpath`.

## Concepts clés

- Balises fréquentes: `<form>`, `<sheet>`, `<group>`, `<field>`, `<notebook>`, `<page>`.
- Widgets (`widget=`) et options (`options=`) côté client.

## Patterns recommandés

- Toujours privilégier une vue “petite” + héritages ciblés plutôt qu’une duplication.
- Utiliser `attrs`/conditions (selon version) pour visibilité/readonly côté UI.

## Pièges fréquents

- XPath trop fragile (change d’une vue standard).
- Modifier une vue standard en remplaçant de gros blocs = maintenance difficile.

## Checklist

- [ ] Créer ou hériter la vue dans `views/*.xml`.
- [ ] Vérifier droits + groups sur fields.
- [ ] Tester en mode debug (voir id de vue, structure).

## Exemples

```xml
<record id="view_x_form" model="ir.ui.view">
  <field name="name">x.model.form</field>
  <field name="model">x.model</field>
  <field name="arch" type="xml">
    <form>
      <sheet>
        <group>
          <field name="name"/>
          <field name="partner_id"/>
        </group>
      </sheet>
    </form>
  </field>
</record>
```

## Voir aussi

- ../view_records/inheritance.md
- ../../server_framework/actions/window_actions_ir_actions_act_window.md
