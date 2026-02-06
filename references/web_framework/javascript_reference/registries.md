# Registries (JS)

Registries are ordered key-value stores used to register components, services, fields, and views. They allow modules to extend the system without tight coupling.

## Main Registries
*   `services`: Global services (rpc, orm, etc.).
*   `fields`: Field components (char, boolean, many2one).
*   `views`: View types (form, list, kanban).
*   `systray`: Icons in the top bar.

## Usage
```javascript
import { registry } from "@web/core/registry";

const myService = { ... };

// Registering
registry.category("services").add("my_service", myService);

// Retrieving
const allServices = registry.category("services").getEntries();
```
