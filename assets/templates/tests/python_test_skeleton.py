# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase

class TestMyModule(TransactionCase):
    def test_something(self):
        rec = self.env["my.model"].create({"name": "X"})
        self.assertTrue(rec)
