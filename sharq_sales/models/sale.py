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

    @api.model_create_multi
    def create(self, vals):
        res = super(sharq_sales, self).create(vals)
        for rec in vals:
            sale_data_dict = {
                'quantity': 0,
                'cost': 0,
                'project_id': rec.get('project_id')
            }
            current_sale_ids = self.search([('project_id', '=', rec.get('project_id'))])
            for current in current_sale_ids:
                print(">>>>>>>>>>>>>", current.qunantity)
                sale_data_dict['quantity'] += current.qunantity
            print("current_sale_idsssssssssssssssssssssssssssssssssssssss", current_sale_ids, self)
        return res

    def write(seld, vals):
        print("\n::::::::::::::::::::::write function called")
 