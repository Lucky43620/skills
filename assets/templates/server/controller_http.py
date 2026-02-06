# -*- coding: utf-8 -*-
from odoo import http

class MyController(http.Controller):

    @http.route("/my_module/hello", auth="user", type="http", website=False)
    def hello(self, **kwargs):
        return "hello"
