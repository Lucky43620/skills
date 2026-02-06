# Patching a Component

You can patch any Owl component registered in Odoo.

## Example
Patching the `ListController` to add a `console.log` on mount.

```javascript
import { ListController } from "@web/views/list/list_controller";
import { patch } from "@web/core/utils/patch";

patch(ListController.prototype, {
    setup() {
        super.setup();
        console.log("List View Mounted!");
    },
    
    createRecord() {
        console.log("About to create");
        return super.createRecord(...arguments);
    }
});
```

*   **Target:** `ListController.prototype` (not the class itself).
*   **Super:** `super.methodName()` calls the original logic.
