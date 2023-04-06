# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sharq_sales(models.Model):
    _name = 'sharq_sales.sharq_sales'
    _description = 'sharq_sales.sharq_sales'
    _rec_name="project_id"
    
    project_id=fields.Many2one('project.project')
    qunantity=fields.Float("Qunantity")
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

    @api.depends('qunantity', 'cost')
    def _sum(self):

        for rec in self:

            rec.update({

                'total': rec.qunantity*rec.cost,

            })
    
    @api.constrains('total')
    def _calc_project_calculations(self):
        for rec in self:
            domain = [('project_id', '=', rec.project_id.id)]
            
            total_sales = 0
            total_expenses = 0
            total_investments = 0
            sale_ids = self.search(domain)
            expense_ids = self.env['sharq.expense'].search(domain)
            investment_ids = self.env['investment.investment'].search(domain)
            for sale_rec in sale_ids:
                # print(">>>>>>>>>>>>>", sale_rec.qunantity)
                total_sales += (sale_rec.qunantity * sale_rec.cost)
            for expense_rec in expense_ids:
                total_expenses += expense_rec.amount
            for invest_rec in investment_ids:
                total_investments += invest_rec.amount
            
            
            rec.project_id.update({
                'totalSale':total_sales,
                'totalExpence':total_expenses,
                'totalInvestment':total_investments,
            })

    # @api.model_create_multi
    # def create(self, vals):
    #     res = super(sharq_sales, self).create(vals)
        
    #     return res

    # def write(seld, vals):
    #     print("\n::::::::::::::::::::::write function called")
 