from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class sharqExpense(models.Model):
    _name = 'sharq.expense'
    _description = 'sharq.expense'

    name = fields.Char()
    project_id = fields.Many2one('project.project')
    line_ids = fields.One2many('sharq.expense.line','expense_id')
    amount = fields.Integer('Amount', compute="_total_bill", store=True)
    date = fields.Date()
    action = fields.Boolean()
    type=fields.Selection(
        selection=[
            ('oli', 'Oli'),
            ('machiner', 'Minchener'),
            ('Misc','Motafirqa')
        ],
        string="Type",
        )
    


    state = fields.Selection(
        selection=[
            ('draft', "Draft"),
            ('approved', "Approved")
        ],
        string="Status",
        default='draft')

    def action_draft(self):
        self.write({'state': 'draft'})

    def action_approved(self):
        if not any(self.line_ids):
            raise ValidationError("At least add one expnse")
        self.write({"state":"approved"})

    @api.constrains('line_ids')
    def _total_bill(self):
        if any(self.line_ids):
            total = 0
            for line in self.line_ids:
                total = total + line.total
            self.amount = total

class ExpenseLine(models.Model):
    _name = 'sharq.expense.line'
    _description = 'sharq.expense.line'

    product_id = fields.Many2one('sharq.product')
    expense_id = fields.Many2one('sharq.expense')
    quantity = fields.Float('Quantity')
    unit_price = fields.Float('Unit Price')
    total = fields.Float('Total', compute='_sum', store=True)
    oilquantity=fields.Float("Oil Quantity")
    oiltotal=fields.Float('Oil Total', compute='_sumOil', store=True)


    @api.depends('quantity', 'unit_price')
    def _sum(self):

        for rec in self:

            rec.update({

                'total': rec.quantity*rec.unit_price,

            })
    @api.depends('oilquantity', 'quantity')
    def _sumOil(self):

        for rec in self:

            rec.update({

                'oiltotal': rec.oilquantity*rec.quantity,

            })

  
    

    