/** @odoo-module **/
import { registry } from "@web/core/registry";

export const myService = {
    dependencies: ["rpc", "notification"],
    start(env, { rpc, notification }) {
        return {
            async ping() {
                notification.add("Ping", { type: "info" });
                return rpc("/my_module/ping", {});
            },
        };
    },
};

registry.category("services").add("my_module.my_service", myService);
