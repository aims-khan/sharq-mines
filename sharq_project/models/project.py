# -*- coding: utf-8 -*-

from odoo import models, fields, api


class project(models.Model):
    _inherit = 'project.project'
    _description = 'project project inherit'
 
    
    product=fields.Char("Mine Product")
    employee_ids=fields.One2many("hr.employee","project_id")
    line_ids=fields.One2many("project.line","project_id")
    # investment_id=fields.Many2one("investment.investment")

    total_expence=fields.Float("Total Expense", readonly="1" )
    total_investment=fields.Float("Total Investment", readonly="1" )
    total_sale=fields.Float("Total Sale", readonly="1" )
    project_start_date = fields.Date(string='Project Start Date')
    project_end_date = fields.Date(string='Project End Date')

    investor_id = fields.Many2one('project.line')
    

class ProjectLine(models.Model):
    _name = 'project.line'
    _description = 'sharq_project.project.line.description'

    #relational fields
    project_id=fields.Many2one("project.project")
    investor_id=fields.Many2one("res.partner")
    investment = fields.Float()
    expense = fields.Float()
    sale = fields.Float()
    profit = fields.Float()




