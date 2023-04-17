from odoo import models, fields, api


class EmployeeInherit(models.Model):
    _inherit= "hr.employee"
    _description = 'sharq_investment.sharq_employee'

    # phone = fields.Char("Phone ")
    salary = fields.Float("Salary")

    project_id = fields.Many2one("project.project")

class HrEmployeePublicInherit(models.Model):
    _inherit = "hr.employee.public"
    _description = "Sharq Employee for extra fields"

    salary = fields.Float("Salary")

    project_id = fields.Many2one("project.project")
    

# class InvestmentLine(models.Model):
#     _name = 'investor.line'
#     _description = 'sharq_investor.investor.line.description'
#     _rec_name="investor_id"

#     amount = fields.Integer("Amount")
#     date=fields.Date()

#     #relational fields
#     investor_id=fields.Many2one("res.partner")
#     investment_id=fields.Many2one("investment.investment")
#     project_id = fields.Many2one('project.project')