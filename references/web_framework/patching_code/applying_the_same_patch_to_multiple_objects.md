# Applying the same patch to multiple objects

Sometimes you want to add the same behavior (e.g., logging, tracking) to multiple classes.

## Helper Function Approach
Create a helper that applies the patch.

```javascript
import { patch } from "@web/core/utils/patch";

function patchWithLogger(ClassToPatch) {
    patch(ClassToPatch.prototype, {
        setup() {
            super.setup();
            console.log("Setup called on", ClassToPatch.name);
        }
    });
}

// Usage
patchWithLogger(ListController);
patchWithLogger(KanbanController);
```

## Loop Approach
If you have a list of classes:
```javascript
const Controllers = [ListController, KanbanController, FormController];

for (const C of Controllers) {
    patch(C.prototype, { ... });
}
```
