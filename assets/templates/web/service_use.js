/** @odoo-module **/
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class UsesMyService extends Component {
    setup() {
        this.myService = useService("my_module.my_service");
    }
}
