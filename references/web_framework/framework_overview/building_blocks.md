# Building Blocks

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html#building-blocks

## TL;DR

Le client web repose sur 4 abstractions principales : Registries, Services, Components et Hooks.

## 1. Registries (Registres)
Des dictionnaires clé/valeur pour stocker des objets (classes, fonctions) accessibles globalement. Essentiel pour l'extensibilité.
*Exemple : `fields`, `views`, `main_components`, `systray`.*

```javascript
import { registry } from "@web/core/registry";
// Ajouter un champ custom
registry.category("fields").add("my_field", MyFieldChar);
```

## 2. Services
Morceaux de code persistants fournissant une fonctionnalité (RPC, Notification, Action, User...). Ils gèrent leurs dépendances (DI).

```javascript
const myService = {
    dependencies: ["notification"],
    start(env, { notification }) {
        // ...
    }
};
registry.category("services").add("myService", myService);
```

## 3. Components & Hooks
- **Components** : Composants Owl standards.
- **Hooks** : Fonctions pour factoriser la logique (mixins fonctionnels).

```javascript
import { useService } from "@web/core/utils/hooks"; // ou directement depuis le core
```
