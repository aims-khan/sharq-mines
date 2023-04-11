# -*- coding: utf-8 -*-

from odoo import models, fields, api
class Invetsor(models.Model):
    _inherit= "res.partner"
    _description = 'inversor.inversor.description'


    district = fields.Char("District")

    invsetor=fields.Boolean("InvSetor", default=True)

class Investment(models.Model):
    _name = 'investment.investment'
    _description = 'sharq_investment.investment'
    
    name = fields.Char("name")
    amount = fields.Integer("Amount"  ,compute='_sum', store=True)
    description=fields.Text("Description")
    active = fields.Boolean(default=True)
    state = fields.Selection(
        [('draft', 'Draft'),
         ('approved', 'Approved'),
        ], 'Status', default='draft', readonly=True,
        help='Choose whether the investment is still approved or not')

    line_ids=fields.One2many("investment.line","investment_id")
    project_id = fields.Many2one('project.project', string='Project', required=True)
    # Add a constraint to ensure that there is only one investment per project
    _sql_constraints = [
        ('project_uniq', 'unique (project_id)', 'An investment already exists for this project.'),
    ]

    @api.constrains('amount')
    def calculate_project_investment(self):
        self.env['sharq_sales.sharq_sales'].project_calculations(self.project_id)


    def action_draft(self):
        self.write({'state':'approved'})

    def action_approved(self):
        self.write({'state': 'draft'})


    @api.constrains('line_ids')
    def _total_amount(self):
            amount = 0
            for line in self.line_ids:
                amount = amount + line.amount
            self.amount = amount


     
class InvestmentLine(models.Model):
    _name = 'investment.line'
    _description = 'sharq_investment.investment.line.description'
    _rec_name="investor_id"

    amount = fields.Integer("Amount")
    date=fields.Date()

    #relational fields
    investor_id=fields.Many2one("res.partner")
    investment_id=fields.Many2one("investment.investment")
