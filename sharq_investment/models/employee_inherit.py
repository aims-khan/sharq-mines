from odoo import models, fields, api


class EmployeeInherit(models.Model):
    _inherit= "hr.employee"
    _description = 'sharq_investment.sharq_employee'

    is_investor = fields.Boolean("Invistor")
    