# Record Rules

## TL;DR

- Les record rules filtrent les records accessibles selon un domaine, par groupe.
- Couche fine : s’applique à read/write/create/unlink selon paramètres.

## Concepts clés

- Modèle `ir.rule` avec champ `domain_force`.
- L’utilisateur superuser (sudo) ignore les rules.

## Patterns recommandés

- Écrire des domains simples, basés sur company, owner, ou relations directes.
- Tester avec un utilisateur standard + multi-company si applicable.

## Pièges fréquents

- Rules qui se contredisent → records invisibles.
- Rules avec `|`/`&` complexes difficiles à maintenir.

## Exemples

```xml
<record id="rule_x_own" model="ir.rule">
  <field name="name">X: only own</field>
  <field name="model_id" ref="model_x_model"/>
  <field name="domain_force">[("create_uid","=",user.id)]</field>
  <field name="groups" eval="[(4, ref('base.group_user'))]"/>
</record>
```

## Voir aussi

- `assets/templates/server/record_rules.xml`
- access_rights.md
