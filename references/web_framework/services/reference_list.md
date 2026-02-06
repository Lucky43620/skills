# Reference List (Services)

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/services.html#reference-list

## Services Communs

| Nom | Import (optionnel pour l'usage) | Description |
| :--- | :--- | :--- |
| **rpc** | `@web/core/network/rpc` | Apples serveur bas niveau (Controllers). |
| **orm** | `@web/core/orm_service` | Apples serveur haut niveau (Models `call`, `searchRead`...). *Préférez l'ORM au RPC.* |
| **user** | `@web/core/user_service` | Infos utilisateur courant (Context, ID, Lang, Timezone...). |
| **notification** | `@web/core/notifications/notification_service` | Afficher des notifications (Toasts). |
| **action** | `@web/webclient/actions/action_service` | Exécuter des actions (`ir.actions`). |
| **http** | `@web/core/network/http_service` | Requêtes HTTP GET/POST brutes. |
| **router** | `@web/core/browser/router_service` | Gestion de l'état de l'URL/Bus. |
| **cookie** | `@web/core/browser/cookie_service` | Gestion des cookies. |
| **effect** | `@web/core/effects/effect_service` | Effets visuels (Rainbow man). |
| **title** | `@web/core/browser/title_service` | Modifier le titre de la page navigateur. |

---

## Détails des APIs

### RPC (`rpc`)
Appel unique `rpc(route, params, settings)`.
Retourne une Promise. Gère les erreurs serveur (code 200 mais avec clé `error`).

```javascript
const data = await rpc("/my/controller", { id: 123 });
```

### User (`user`)
Fournit le contexte utilisateur essentiel pour les appels serveur.

- `context` : Objet context (lang, allowed_companies...).
- `userId`, `partnerId`, `name`, `isAdmin`.
- `hasGroup(xmlId)` : Vérifie l'appartenance à un groupe (Async).

### Notification (`notification`)
Affiche un toast.

```javascript
notification.add("Message", {
    title: "Titre",
    type: "success", // warning, danger, info
    sticky: false,
});
```

### HTTP (`http`)
Pour des besoins spécifiques hors RPC/ORM (ex: télécharger un blob).

```javascript
await http.get("https://external.api/data");
await http.post("/route", { ...formData });
```
