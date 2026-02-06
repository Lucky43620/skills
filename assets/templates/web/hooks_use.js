/** @odoo-module **/
import { Component } from "@odoo/owl";
import { useBus, useAutofocus } from "@web/core/utils/hooks";

export class HookExample extends Component {
    setup() {
        useAutofocus();
        useBus(this.env.bus, "my-event", () => {});
    }
}
