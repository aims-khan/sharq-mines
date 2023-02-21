# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class ProjectInherit(models.Model):
#     _inherit = 'project.project'
#     _description = 'project.project.inherit'

#     def action_view_tasks(self):
#         action = self.with_context(active_id=self.id, active_ids=self.ids) \
#             .env.ref('project.edit_project') \
#             .sudo().read()[0]
#         action['display_name'] = self.name
#         action['type'] = '[tree,form]'
#         return action

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
