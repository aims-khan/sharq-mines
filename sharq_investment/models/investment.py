# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Investment(models.Model):
    _name = 'investment.investment'
    _description = 'sharq_investment.investment'
    
    name = fields.Char("name")
    amount = fields.Integer("Amount")
    description=fields.Text("Description")
    active = fields.Boolean(default=True)
    state = fields.Selection(
        [('draft', 'Draft'),
         ('approved', 'Approved'),
        ], 'Status', default='draft', readonly=True,
        help='Choose whether the investment is still approved or not')

    #relational fields
    # employee_id=fields.Many2one("hr.employee")
    # line = fields.Many2one("project.project")
    line_ids=fields.One2many("investment.line","investment_id")


    def action_draft(self):
        self.write({'state':'approved'})

    def action_approved(self):
        self.write({'state': 'approved'})

class InvestmentLine(models.Model):
    _name = 'investment.line'
    _description = 'sharq_investment.investment.line.description'
    _rec_name="employee_id"

    amount = fields.Integer("Amount")
    date=fields.Date()
    # state = fields.Selection(
    #     [('draft', 'Draft'),
    #      ('approved', 'Approved')
    #     ], 'Status', default='draft', readonly=True,
    #     help='Choose whether the investment is still approved or not')

    #relational fields
    employee_id=fields.Many2one("hr.employee")
    investment_id=fields.Many2one("investment.investment")


    # def action_draft(self):
    #     self.write({'state':'draft'})

    # def action_approved(self):
    #     self.write({'state': 'approved'})
