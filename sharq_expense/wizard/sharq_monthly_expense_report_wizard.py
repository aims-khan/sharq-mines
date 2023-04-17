# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SharqExpenseWizard(models.TransientModel):
    _name = 'sharq.expense.report.wizard'
    _description = 'sharq.expense.report.wizard'


    project_ids = fields.Many2many('project.project')
    start_date = fields.Date("Start Date")
    end_date = fields.Date("End Date")

    def print_montly_expense_report(self):
        data = {
            'wizard_data': self.read()[0],
        }
        return self.env.ref('sharq_expense.action_monthly_expense_report').report_action(self, data=data)

