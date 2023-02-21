from odoo import models, fields, api


class EmployeeInherit(models.Model):
    _inherit= "hr.employee"
    _description = 'sharq_investment.sharq_employee'

    is_invistor = fields.Boolean("Invistor")
    