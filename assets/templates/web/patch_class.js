/** @odoo-module **/
import { patch } from "@web/core/utils/patch";

patch(SomeClass.prototype, "my_module.some_patch", {
    someMethod() {
        return this._super(...arguments);
    },
});
