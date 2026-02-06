/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";

/**
 * Exemple minimal de widget de champ OWL.
 * ⚠️ À adapter selon API des field widgets en v19 (voir doc/implémentations core).
 */

class MyWidget extends Component {}
MyWidget.template = "my_addon.MyWidget";

registry.category("fields").add("my_widget", {
  component: MyWidget,
});
