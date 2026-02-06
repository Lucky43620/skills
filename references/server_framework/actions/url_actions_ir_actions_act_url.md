# URL Actions (ir.actions.act_url)

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/actions.html

## TL;DR

- `ir.actions.act_url` ouvre une URL externe ou interne dans le client web.
- Utile pour rediriger vers une page de documentation, un service externe ou une vue.

## Quand l’utiliser

- Pour ouvrir une URL externe depuis un menu ou un bouton.
- Pour naviguer vers un lien interne dynamique (ex: page website).

## Concepts clés

- **`url`** : URL cible (interne ou externe).
- **`target`** : comportement d’ouverture (nouvel onglet ou même fenêtre).

## API / Syntaxe

```xml
<!-- my_module/views/actions.xml -->
<record id="action_open_docs" model="ir.actions.act_url">
  <field name="name">Documentation</field>
  <field name="url">https://www.odoo.com/documentation/19.0/</field>
  <field name="target">new</field>
</record>
```

## Patterns recommandés

- Utiliser `target="new"` pour les URLs externes.
- Garder l’URL configurable via un paramètre système si besoin.

## Anti-patterns & pièges

- URL hardcodée vers un environnement non stable (ex: staging).
- Utiliser une action URL pour un besoin couvert par une action fenêtre.

## Debug & troubleshooting

- Vérifier que l’URL est accessible depuis le navigateur.
- Contrôler la présence de l’action dans les menus/accès.

## Exemples complets

```xml
<!-- my_module/views/menu.xml -->
<menuitem id="menu_docs" name="Docs" action="action_open_docs"/>
```

## Checklist

- [ ] URL valide et stable.
- [ ] `target` adapté (nouvel onglet vs même fenêtre).
- [ ] Action correctement liée à un menu si nécessaire.

## Liens officiels

- https://www.odoo.com/documentation/19.0/developer/reference/backend/actions.html

## Voir aussi

- [Actions (index)](index.md)
- [Window actions](window_actions_ir_actions_act_window.md)
- [Client actions](client_actions_ir_actions_client.md)
