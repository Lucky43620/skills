# Server Actions (ir.actions.server)

## TL;DR

- Permet d’exécuter du code (Python) côté serveur depuis l’UI (automation, bouton, etc.).
- Peut être binding à un modèle ou déclenchée par un cron.

## Patterns recommandés

- Préférer appeler une méthode de modèle (`model.method()`) plutôt que d’écrire beaucoup de code inline.
- Limiter `sudo()`; respecter les droits autant que possible.

## Pièges fréquents

- Code inline difficile à versionner/tester.

## Exemples

```xml
<record id="action_server_x" model="ir.actions.server">
  <field name="name">Do X</field>
  <field name="model_id" ref="model_x_model"/>
  <field name="state">code</field>
  <field name="code">records._do_x()</field>
</record>
```
