# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from odoo.exceptions import UserError, ValidationError


class sharq_sales(models.Model):
    _name = 'sharq_sales.sharq_sales'
    _description = 'sharq_sales.sharq_sales'
    _rec_name="project_id"
    
    project_id=fields.Many2one('project.project')
    quantity=fields.Float("Quantity")
    date=fields.Date("Date")
    cost=fields.Integer("Cost")
    description = fields.Text()
    total = fields.Integer("Sale"  ,compute='_sum', store=True)
    state = fields.Selection(
        [('draft', 'Draft'),
         ('approved', 'Approve'),
        ], 'Status', default='draft', readonly=True,
        help='Choose whether the investment is still approved or not')

    def action_draft(self):
        self.write({'state':'approved'})

    def action_approved(self):
        self.write({'state': 'draft'})

    @api.depends('quantity', 'cost')
    def _sum(self):

        for rec in self:

            rec.update({

                'total': rec.quantity*rec.cost,

            })
    @api.constrains('project_id')
    def _check_investment(self):
        # project_id = self.project_id
        investment_ids = self.env['investment.investment'].search([('project_id', '=', self.project_id.id)])
        if not investment_ids:
            raise ValidationError(("There are no investments for the selected project. You cannot proceed with the sale."))
    
    @api.constrains('total')
    def calc_project_calculations(self):
        for rec in self:
            # project_id = rec.project_id
            self.project_calculations(self.project_id) 
    
    def project_calculations(self, project_id=False):
        if not project_id:
            project_id = self.project_id
        domain = [('project_id', '=', project_id.id)]
        investor_dict = {}
        total_sales = 0
        total_expenses = 0
        total_investments = 0
        sale_ids = self.env['sharq_sales.sharq_sales'].search(domain)
        expense_ids = self.env['sharq.expense'].search(domain)
        investment_ids = self.env['investment.investment'].search(domain)
        project_line_obj = self.env['project.line']
        # project_line_ids = []
        for sale_rec in sale_ids:
            total_sales += (sale_rec.quantity * sale_rec.cost)
        for expense_rec in expense_ids:
            total_expenses += expense_rec.amount
        for invest_rec in investment_ids:
            total_investments += invest_rec.amount
            for line in invest_rec.line_ids:
                if not investor_dict.get(line.investor_id.id):
                    investor_dict[line.investor_id.id] = line.amount
                elif investor_dict.get(line.investor_id.id):
                    investor_dict[line.investor_id.id] += line.amount
            # investor_dict
        for investor, investment in investor_dict.items():
            project_line_id = project_line_obj.create({
                'project_id': project_id.id,
                'investor_id': investor,
                'investment': investment,
                # total money from profit of project here we should calculate amount of the profit of the project total_sale-total_investment instead of 200000
                'sale': (((100*investment)/total_investments)*(total_sales-total_investments))/100 if total_sales else 0,
                # total expance belonges to a persone
                'expense': (((100*investment)/total_investments)*total_expenses)/100 if total_expenses else 0,
                # percentage in project
                'profit': (100*investment)/total_investments if total_sales else 0,
            })
        project_id.write({
            'total_sale': total_sales,
            'total_expence': total_expenses,
            'total_investment': total_investments,
        })

