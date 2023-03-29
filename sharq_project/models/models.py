# -*- coding: utf-8 -*-

from odoo import models, fields, api


class project(models.Model):
    _inherit = 'project.project'
    _description = 'project project inherit'
 
    employee_ids=fields.One2many("hr.employee","project_id")
    product=fields.Char("Mine Product")

