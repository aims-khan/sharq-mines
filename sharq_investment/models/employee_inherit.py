from odoo import models, fields, api


class EmployeeInherit(models.Model):
    _inherit= "hr.employee"
    _description = 'sharq_investment.sharq_employee'

    phone =fields.Char("Phone ")