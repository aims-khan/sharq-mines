# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
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
    project_id = fields.Many2one('project.project')

    @api.constrains('amount')
    def calculate_project_investment(self):
        self.env['sharq_sales.sharq_sales'].project_calculations(self.project_id)
 

    # def check_deleted_investment(self, investment_id):
    #     models_to_check = ['sharq_sales.sharq_sales', 'sharq.expense', 'project.line']
    #     for model_name in models_to_check:
    #         model = self.env[model_name]
    #         related_records = model.search([('investment_id', '=', investment_id)])
    #         if related_records:
    #             # If there are related records, you can either update or delete them depending on your requirements.
    #             # For example, to update the foreign key to None:
    #             related_records.write({'investment_id': None})
    # @api.multi
    # def unlink(self):
    #     for investment in self:
    #         # Check if the investment is referenced by any other objects
    #         sale_ids = self.env['sharq_sales.sharq_sales'].search([('investment_id', '=', investment.id)])
    #         expense_ids = self.env['sharq.expense'].search([('investment_id', '=', investment.id)])
    #         project_line_ids = self.env['project.line'].search([('investment_id', '=', investment.id)])
    #         if sale_ids or expense_ids or project_line_ids:
    #             # Investment is referenced by other objects, raise an error or update/delete them accordingly
    #             # For example, you can raise an error and prevent the deletion of the investment:
    #             raise ValidationError('Cannot delete investment that is referenced by sales, expenses, or project lines')
    #         else:
    #             # Investment is not referenced by any other objects, proceed with deletion
    #             super(Investment, investment).unlink()
    #     return True

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
