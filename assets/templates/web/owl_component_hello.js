/** @odoo-module **/

import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class Hello extends Component {
  setup() {
    this.notification = useService("notification");
  }
  sayHi() {
    this.notification.add("Salut !");
  }
}
Hello.template = "my_addon.Hello";
