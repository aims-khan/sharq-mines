# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


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
    @api.constrains('project_id')
    def _check_investment(self):
        # project_id = self.project_id
        investment_ids = self.env['investment.investment'].search([('project_id', '=', self.project_id.id)])
        if not investment_ids:
            raise ValidationError(("There are no investments for the selected project. You cannot proceed with the sale."))
    
    @api.constrains('total')
    def calc_project_calculations(self):
        for rec in self:
            # project_id = project_id if project_id else rec.project_id
            self.project_calculations(self.project_id) 
    

    def project_calculations(self, project_id=False):
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
            # print(">>>>>>>>>>>>>", sale_rec.qunantity)
            total_sales += (sale_rec.qunantity * sale_rec.cost)
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
        project_id.write({'line_ids': [(5)]})
        for investor, investment in investor_dict.items():
            print(">>>>>>>>investor>>>>>>>>", investor, investment)
            project_line_id = project_line_obj.create({
                'project_id': project_id.id,
                'investor_id': investor,
                'investment': investment,
                'expense': (investment/total_expenses)*investment,
                'sale': (investment/total_investments)*investment,
                'profit': 0,
            })
            # project_line_ids.append(project_line_id.id)
            # print(":::::::::::::::::project_id:::::::::::::::::::", project_line_ids)
            # project_id.write({
            # })
        

        project_id.write({
            'total_sale': total_sales,
            'total_expence': total_expenses,
            'total_investment': total_investments,
            # 'line_ids': [(6, 0, [project_line_ids])],
            # 'line_ids': 
        })


    

   
    # @api.model_c
    # 
    # reate_multi
    # def create(self, vals):
    #     res = super(sharq_sales, self).create(vals)
        
    #     return res

    # def write(seld, vals):
    #     print("\n::::::::::::::::::::::write function called")
 