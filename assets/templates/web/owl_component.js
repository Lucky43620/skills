/** @odoo-module **/

import { Component, useState } from "@odoo/owl";

export class MyWidget extends Component {
    static template = "my_module.MyWidget";

    setup() {
        this.state = useState({ count: 0 });
    }

    increment() {
        this.state.count += 1;
    }
}
