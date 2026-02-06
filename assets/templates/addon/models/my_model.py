# -*- coding: utf-8 -*-
from odoo import api, fields, models

class MyModel(models.Model):
    _name = "my.model"
    _description = "My Model"

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        return records
