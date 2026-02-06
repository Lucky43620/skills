# Defining a Service

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/services.html#defining-a-service

## TL;DR
Un service est un objet standard avec une méthode `start(env, deps)`.
Il doit être enregistré dans le registre `services`.

## Structure

```javascript
import { registry } from "@web/core/registry";

const myService = {
    // 1. Dépendances (ex: "rpc", "notification", "user")
    dependencies: ["rpc", "notification"],

    // 2. Méthode start (asynchrone ou synchrone)
    async start(env, { rpc, notification }) {
        let someState = 0;

        // Logique d'initialisation...
        console.log("Service démarré");

        // 3. API Publique (ce que le service expose)
        return {
            doSomething() {
                someState++;
                notification.add("Action effectuée !");
            },
            getValue() {
                return someState;
            }
        };
    }
};

// 4. Enregistrement
registry.category("services").add("my_service", myService);
```

## Options Avancées
- `async`: `true` ou liste de méthodes strings. Permet de protéger les appels asynchrones si le composant appelant est détruit entre temps.
