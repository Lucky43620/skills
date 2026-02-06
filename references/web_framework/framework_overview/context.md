# Context

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html

## TL;DR

- Le `context` est un dictionnaire transmis aux actions, vues et RPC.
- Il transporte des flags fonctionnels (langue, tz, defaults).

## Quand l’utiliser

- Pour fournir des valeurs par défaut ou filtrer des comportements.
- Pour aligner front et server via `context` dans les appels ORM.

## Concepts clés

- `context` est fusionné (session + action + view + caller).
- Les clés standard (`lang`, `tz`, `uid`) coexistent avec des clés métier.

## API / Syntaxe

- ORM JS : `this.env.services.orm.call(model, method, args, { context })`.
- Action : `this.env.services.action.doAction(action, { additionalContext })`.

## Patterns recommandés

- Nommer les clés custom en préfixant (`my_module_...`).
- Éviter d’écraser des clés standards.

## Anti-patterns & pièges

- Passer des objets lourds dans le `context`.
- Utiliser le `context` comme stockage persistant.

## Debug & troubleshooting

- Inspecter `action.context` dans le mode debug.
- Logger le `context` au niveau des `rpc`.

## Exemples complets

```javascript
// my_module/static/src/js/open_partner.js
/** @odoo-module **/

export async function openPartner(env, partnerId) {
    await env.services.action.doAction("base.action_partner_form", {
        additionalContext: {
            default_is_company: true,
            my_module_source: "dashboard",
        },
        additionalDomain: [["id", "=", partnerId]],
    });
}
```

## Checklist

- [ ] Les clés custom sont préfixées.
- [ ] Les `context` sont limités à des données légères.
- [ ] Les actions vérifient les clés attendues.

## Liens officiels

- https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html

## Voir aussi

- [Actions JS](../javascript_reference/client_actions.md)
- [Services](../services.md)
- [ORM API (server)](../../server_framework/orm_api.md)
