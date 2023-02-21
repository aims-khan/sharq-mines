# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Investment(models.Model):
    _name = 'investment.investment'
    _description = 'sharq_investment.investment'
    _rec_name="employee_id"

    amount = fields.Integer("Amount")
    active = fields.Boolean(default=True)
    state = fields.Selection([('draft','Draft'),('approved','Approved'),],
        readonly=True,
        default='draft' 
    )

    #relational fields
    employee_id=fields.Many2one("hr.employee")


    def action_draft(self):
        self.write({'state':'draft'})

    def action_approved(self):
        self.write({'state': 'approved'})

