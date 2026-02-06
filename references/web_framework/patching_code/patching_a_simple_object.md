# Patching a Simple Object

You can also patch plain Javascript objects (instances), not just prototypes.

## Usage
Only the specific instance is modified.

```javascript
import { patch } from "@web/core/utils/patch";

const myObj = {
    sayHello() {
        return "Hello";
    }
};

patch(myObj, {
    sayHello() {
        return super.sayHello() + " World";
    }
});

console.log(myObj.sayHello()); // "Hello World"
```

## Use Case
*   Patching a specific `service` instance exported by a module (if it's not a class).
*   Patching global singletons (rare/discouraged).
