# Bindings

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/actions.html

## TL;DR

- Les `bindings` relient une action à un modèle et/ou à des vues pour l’afficher dans le menu ou l’UI contextuelle.
- Utiles pour exposer des actions depuis la barre d’actions, les menus ou les vues.

## Quand l’utiliser

- Pour afficher une action dans le menu d’un modèle (impression, action serveur, action client).
- Pour restreindre l’action à certains types de vues (liste, formulaire, kanban).

## Concepts clés

- **Action liée** : action associée à un modèle via des champs de binding.
- **Point d’entrée UI** : barre d’actions, menu, bouton, menu contextuel.
- **Types de vues** : l’action peut être disponible seulement sur certaines vues.

## API / Syntaxe

- Les actions supportant le binding exposent des champs dédiés (ex: `binding_model_id`, `binding_view_types`).
- L’action est déclarée via XML dans `my_module/views/*.xml`.

```xml
<!-- my_module/views/actions.xml -->
<record id="action_my_server" model="ir.actions.server">
  <field name="name">Traitement</field>
  <field name="model_id" ref="model_res_partner"/>
  <field name="state">code</field>
  <field name="code">records._my_process()</field>
  <field name="binding_model_id" ref="model_res_partner"/>
  <field name="binding_view_types">list,form</field>
</record>
```

## Patterns recommandés

- Lier l’action au modèle pour l’afficher dans la barre d’actions.
- Limiter `binding_view_types` aux vues où l’action est pertinente.
- Placer la logique métier dans des méthodes Python et garder l’action XML minimale.

## Anti-patterns & pièges

- Action liée sans vérification des droits (`sudo()` inutile).
- Action disponible partout alors qu’elle ne s’applique qu’à un type de vue.

## Debug & troubleshooting

- Vérifier que l’action apparaît dans la barre d’actions de la vue ciblée.
- Contrôler que le modèle et les vues ciblées sont chargés dans la base.
- Tester avec `?debug=1` pour inspecter les actions disponibles.

## Exemples complets

```python
# my_module/models/res_partner.py
from odoo import models

class ResPartner(models.Model):
    _inherit = "res.partner"

    def _my_process(self):
        for partner in self:
            partner.message_post(body="Traitement lancé")
```

```xml
<!-- my_module/views/actions.xml -->
<record id="action_my_server" model="ir.actions.server">
  <field name="name">Traitement</field>
  <field name="model_id" ref="model_res_partner"/>
  <field name="state">code</field>
  <field name="code">records._my_process()</field>
  <field name="binding_model_id" ref="model_res_partner"/>
  <field name="binding_view_types">list,form</field>
</record>
```

## Checklist

- [ ] L’action est liée au bon modèle via `binding_model_id`.
- [ ] Les types de vues sont filtrés via `binding_view_types`.
- [ ] La logique métier est dans un modèle Python.

## Liens officiels

- https://www.odoo.com/documentation/19.0/developer/reference/backend/actions.html

## Voir aussi

- [Actions (index)](index.md)
- [Server actions](server_actions_ir_actions_server.md)
- [Window actions](window_actions_ir_actions_act_window.md)
- [Report actions](report_actions_ir_actions_report.md)
- [URL actions](url_actions_ir_actions_act_url.md)
