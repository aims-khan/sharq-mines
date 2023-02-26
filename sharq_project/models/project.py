# -*- coding: utf-8 -*-

from odoo import models, fields, api


class projectbudget(models.Model):
    _inherit = 'project.project'
    _description = 'project.project'

    emloyee_ids = fields.One2many("hr.employee","project_id")


