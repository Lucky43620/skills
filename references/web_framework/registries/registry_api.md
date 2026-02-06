# Registry API

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/registries.html#registry-api

## TL;DR

Les registres sont des bus d'événements ordonnés stockant des paires clé/valeur.
Ils sont le mécanisme principal d'extension du framework JS.

## Méthodes

### `add(key, value, options)`
Insère une valeur.
- **options.force** (boolean) : Écrase si la clé existe déjà.
- **options.sequence** (number) : Position (trié par `getAll`).

```javascript
import { registry } from "@web/core/registry";
registry.category("fields").add("my_field", MyField, { sequence: 10 });
```

### `get(key, defaultValue)`
Récupère une valeur.
- Si `defaultValue` n'est pas fourni et la clé manque -> **Error**.

### `contains(key)`
Retourne `true` si la clé existe.

### `getAll()`
Retourne la liste des **valeurs** (pas les clés) triées par séquence.

### `remove(key)`
Supprime une entrée. Déclenche un événement `UPDATE`.

### `category(subcategory)`
Retourne un sous-registre (créé à la volée s'il n'existe pas).

```javascript
const serviceRegistry = registry.category("services");
serviceRegistry.add(...);
```
