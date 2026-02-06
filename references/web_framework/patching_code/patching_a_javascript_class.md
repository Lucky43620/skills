# Patching a Javascript Class

For standard classes (not Components), you also patch the prototype.

## Example
Patching a utility class.

```javascript
import { SomeClass } from "@some_module/some_file";
import { patch } from "@web/core/utils/patch";

patch(SomeClass.prototype, {
    doSomething(arg) {
        if (arg > 10) {
            console.log("Big number!");
        }
        return super.doSomething(arg);
    }
});
```
