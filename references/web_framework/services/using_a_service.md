# Using a Service

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/services.html#using-a-service

## TL;DR
Utilisez le hook `useService("nom_du_service")` à l'intérieur de `setup()`.

## Dans un Composant

```javascript
import { Component, onWillStart } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

class MyComponent extends Component {
    setup() {
        // 1. Récupérer le service
        this.rpc = useService("rpc");
        this.user = useService("user");
        this.notification = useService("notification");

        // 2. Utiliser (exemple d'appel async au démarrage)
        onWillStart(async () => {
            this.data = await this.rpc("/my/route");
        });
    }

    handleClick() {
        // Utilisation ponctuelle
        this.notification.add("Bouton cliqué !");
    }
}
```

## Dans un autre Service
Déclarez le service requis dans `dependencies` et récupérez-le dans les arguments de `start`.

```javascript
const myService = {
    dependencies: ["user"],
    start(env, { user }) {
        console.log("Current user:", user.name);
    }
};
```
