from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class sharqExpense(models.Model):
    _name = 'sharq.expense'
    _description = 'sharq.expense'

    name = fields.Char()
    amount = fields.Integer('Amount', compute="_total_bill", store=True)
    reminder = fields.Integer('Reminder', compute="_total_reminder", store=True)
    payed = fields.Integer('Paid',compute="_total_payed", store=True)
    date = fields.Date()
    action = fields.Boolean()
    
    descripation = fields.Text("Descripation")

    # Relational Fields
    project_id = fields.Many2one('project.project')
    line_ids = fields.One2many('sharq.expense.line','expense_id')

    @api.constrains('project_id')
    def _check_investment(self):
        if not self.project_id:
            return
        investment_ids = self.env['investment.investment'].search([('project_id', '=', self.project_id.id)])
        if not investment_ids:
            raise ValidationError("There are no investments for the selected project. You cannot proceed with the sale.")

    
    
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
                total = total + line.reminder
            self.reminder = total


    @api.constrains('line_ids')
    def _total_reminder(self):
        if any(self.line_ids):
            total = 0
            for line in self.line_ids:
                total = total + line.total
            self.amount = total

    @api.constrains('line_ids')
    def _total_payed(self):
        if any(self.line_ids):
            total = 0
            for line in self.line_ids:
                total = total + line.payed
            self.payed = total
    

     
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
    bill = fields.Char('Bill Number')
    payed = fields.Integer('Padyed')
    reminder = fields.Integer('Reminder', compute="_total_reminder", store=True)
    date = fields.Date(string="Date")
    descripation = fields.Char("Descripation")


    @api.depends('quantity', 'unit_price')
    def _sum_quantity_unit_price(self):
        for rec in self:
            rec.update({
                    'total': rec.quantity*rec.unit_price,
                })
            

    @api.depends('total')
    def _total_reminder(self):
        for record in self:
            total = record.total-record.payed
            record.reminder = total

 
    @api.depends('oil_quantity', 'quantity')
    def _total_oil_expance(self):
        for rec in self:
            rec.update({
                'oil_total': rec.oil_quantity*rec.quantity,
            })
    

    