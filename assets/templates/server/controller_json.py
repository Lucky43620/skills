# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class MyJsonRpcController(http.Controller):

    # Odoo v19: préférer type="jsonrpc"
    @http.route("/my_module/ping", auth="user", type="jsonrpc")
    def ping(self, **kwargs):
        return {"ok": True}
