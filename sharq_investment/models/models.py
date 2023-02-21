# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sharq_investment(models.Model):
    _name = 'sharq_investment.sharq_investment'
    _description = 'sharq_investment.sharq_investment_des'

    name = fields.Char("name")
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
