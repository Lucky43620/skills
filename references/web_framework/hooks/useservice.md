# useService

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/services.html#using-services

Le hook `useService` est le moyen standard d'accéder aux services globaux d'Odoo (ORM, RPC, Notifications, Actions, etc.) depuis un composant Owl.

## Usage

```javascript
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class MyComponent extends Component {
    setup() {
        this.orm = useService("orm");
        this.action = useService("action");
        this.notification = useService("notification");
    }

    async saveData() {
        // Ex: Appel ORM
        await this.orm.call("res.partner", "write", [[this.props.partnerId], { name: "New Name" }]);
        
        // Ex: Notification
        this.notification.add("Sauvegarde réussie", { type: "success" });
        
        // Ex: Action
        this.action.doAction("account.action_account_moves_all");
    }
}
```

## Services Communs

| Service | Clé | Usage |
| :--- | :--- | :--- |
| **ORM** | `"orm"` | Appels `call`, `searchRead`, `create`, `write`. |
| **RPC** | `"rpc"` | Appels bruts JSON-RPC (préférer `orm` pour les modèles). |
| **Action** | `"action"` | Exécuter des actions (`doAction`). |
| **Notification** | `"notification"` | Afficher des toasts (`add`). |
| **User** | `"user"` | Infos user courant (`userId`, `hasGroup`). |
| **Router** | `"router"` | Manipulation de l'URL/Routing. |
| **PWA** | `"pwa"` | Install prompt, offline detection (Enterprise). |
