# Window Actions (ir.actions.act_window)

## TL;DR

- Action la plus courante : ouvre une vue (tree/form/kanban…) sur un modèle.
- Associée à un menu (`ir.ui.menu`) et éventuellement à des bindings.

## Concepts clés

- Champs clés : `res_model`, `view_mode`, `domain`, `context`, `views`.
- Peut cibler un record spécifique via `res_id`.

## Patterns recommandés

- Mettre domain/context en dur quand c’est stable; sinon calculer via server action ou action dynamique.
- Déclarer `view_mode` dans l’ordre souhaité (ex: `tree,form`).

## Pièges fréquents

- Domain mal écrit (tuple vs liste) ou champs non stockés → lenteur/erreur.
- Context qui force une company/lang inattendue.

## Exemples

```xml
<record id="action_x" model="ir.actions.act_window">
  <field name="name">X</field>
  <field name="res_model">x.model</field>
  <field name="view_mode">tree,form</field>
  <field name="domain">[("active","=",True)]</field>
</record>

<menuitem id="menu_x" name="X" action="action_x"/>
```

## Voir aussi

- `assets/templates/server/action_window.xml`
- ../../user_interface/view_architectures/form.md
