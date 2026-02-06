# Scheduled Actions (ir.cron)

## TL;DR

- Tâche planifiée exécutée par le scheduler Odoo.
- Déclenche une méthode python sur un modèle selon intervalle.

## Concepts clés

- Champs : interval_number/type, numbercall, active, doall, nextcall.

## Pièges fréquents

- Job non idempotent → effets de bord si relancé.
- Performances : éviter de traiter trop de données en une seule exécution.

## Exemples

```xml
<record id="cron_my_job" model="ir.cron">
  <field name="name">My Job</field>
  <field name="model_id" ref="model_x_model"/>
  <field name="state">code</field>
  <field name="code">model._my_job()</field>
  <field name="interval_number">1</field>
  <field name="interval_type">hours</field>
</record>
```

## Voir aussi

- `assets/templates/server/scheduled_action_cron.xml`
