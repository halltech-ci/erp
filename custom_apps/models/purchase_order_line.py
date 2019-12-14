# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class custom_apps(models.Model):
#     _name = 'custom_apps.custom_apps'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    
    item = fields.Char(string="Item", store=False)