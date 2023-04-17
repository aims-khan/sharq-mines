from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class sharqExpense(models.Model):
    _name = 'sharq.expense'
    _description = 'sharq.expense'

    name = fields.Char()
    amount = fields.Integer('Amount', compute="_total_bill", store=True)
    date = fields.Date()
    action = fields.Boolean()

    # Relational Fields
    project_id = fields.Many2one('project.project')
    line_ids = fields.One2many('sharq.expense.line','expense_id')


    
    
    @api.constrains('amount')
    def calculate_project_expense(self):
        self.env['sharq_sales.sharq_sales'].project_calculations(self.project_id)

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
    total = fields.Float('Total', compute='_sum_quantity_unit_price', store=True)
    oil_quantity=fields.Float("Oil Quantity")
    oil_total=fields.Float('Oil Total', compute='_total_oil_expance', store=True)


    @api.depends('quantity', 'unit_price')
    def _sum_quantity_unit_price(self):
        for rec in self:
            rec.update({
                    'total': rec.quantity*rec.unit_price,
                })
 
    @api.depends('oil_quantity', 'quantity')
    def _total_oil_expance(self):
        for rec in self:
            rec.update({
                'oil_total': rec.oil_quantity*rec.quantity,
            })
    

    
