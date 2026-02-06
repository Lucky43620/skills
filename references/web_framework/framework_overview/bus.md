# Bus (EventBus)

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html#bus

## TL;DR

Le `env.bus` est un bus d'événements global pour coordonner l'interface sans couplage fort.

## Usage

```javascript
// Écouter un événement
env.bus.on("WEB_CLIENT_READY", null, () => {
    console.log("Odoo is ready");
});

// Déclencher (rare pour le dev standard, plutôt réservé au framework)
env.bus.trigger("MY_EVENT", payload);
```

## Événements Principaux

| Événement | Payload | Description |
| :--- | :--- | :--- |
| `WEB_CLIENT_READY` | - | Le WebClient est monté. |
| `RPC:REQUEST` | rpcId | Une requête RPC démarre. |
| `RPC:RESPONSE` | rpcId | Une requête RPC est terminée. |
| `route_change` | - | L'URL (hash) a changé. |
| `ACTION_MANAGER:UI-UPDATED` | mode | L'interface d'action a été mise à jour. |
| `MENUS:APP-CHANGED` | - | L'utilisateur a changé d'application racine. |
| `CLEAR-CACHES` | - | Demande de vider les caches locaux. |
