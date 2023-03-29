# -*- coding: utf-8 -*-

from odoo import models, fields, api


class project(models.Model):
    _inherit = 'project.project'
    _description = 'project project inherit'
 
    employee_ids=fields.One2many("hr.employee","project_id")
    line_ids=fields.One2many("project.line","project_id")
    product=fields.Char("Mine Product")






class ProjectLine(models.Model):
    _name = 'project.line'
    _description = 'sharq_project.project.line.description'
    _rec_name="investor_id"

    part=fields.Float("Part")

    #relational fields
    investor_id=fields.Many2one("res.partner")
    project_id=fields.Many2one("project.project")
    expense_id=fields.Many2one("sharq.expense")
    sale_id=fields.Many2one("sharq_sales.sharq_sales")
    
    

