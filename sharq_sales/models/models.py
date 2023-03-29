# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sharq_sales(models.Model):
    _name = 'sharq_sales.sharq_sales'
    _description = 'sharq_sales.sharq_sales'
    _rec_name="project_id"
    
    project_id=fields.Many2one('project.project')
    qunantity=fields.Float("Qunantity")
    date=fields.Date("Date")
    cost=fields.Float("Cost")
    description = fields.Text()
    total = fields.Integer("Total"  ,compute='_sum', store=True)
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