# -*- coding: utf-8 -*-

from odoo import models, fields, api


class employees(models.Model):
    _inherit = 'hr.employee'
    _description = 'project.project'
    
    project_id = fields.Many2one("project.project")
    salary=fields.Integer("Salary")

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
