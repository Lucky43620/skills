/** @odoo-module **/
import { patch } from "@web/core/utils/patch";

patch(SomeOwlComponent.prototype, "my_module.patch_component", {
    setup() {
        this._super(...arguments);
        // ...
    },
});
