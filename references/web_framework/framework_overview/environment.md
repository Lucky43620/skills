# Environment (JS)

In the Odoo Web Framework (Owl), the **Environment** is a central object that contains all the active services and the event bus. It is accessible from any component.

## Accessing the Environment

### In a Component
```javascript
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

class MyComponent extends Component {
    setup() {
        // Access a specific service
        this.rpc = useService("rpc");
        
        // Access the raw environment (rarely needed directly)
        console.log(this.env);
    }
}
```

## Contents
The environment typically contains:
*   `services`: The registry of active services (orm, rpc, action, etc.).
*   `bus`: The main event bus for the application.
*   `qweb`: The rendering engine context.
*   `_t`: The translation function.

## Hierarchy
The environment is propagated down the component tree. A component can create a *child environment* to override specific values for its descendants, though this is an advanced use case.
