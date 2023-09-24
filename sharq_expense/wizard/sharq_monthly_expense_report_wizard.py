# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SharqExpenseWizard(models.TransientModel):
    _name = 'sharq.expense.report.wizard'
    _description = 'sharq.expense.report.wizard'


    project_ids = fields.Many2many('project.project')
    start_date = fields.Date("Start Date")
    end_date = fields.Date("End Date")

    def print_montly_expense_report(self):
        domain = [('active', '=', True)]
        if self.project_ids.ids and self.start_date and self.end_date:
            domain.append(('id', 'in', self.project_ids.ids), ('date', '>=', self.start_date), ('date', '<=', self.end_date))
        elif self.project_ids.ids and not self.start_date and not self.end_date:
            domain.append(('id', 'in', self.project_ids.ids))
        elif not self.project_ids.ids and self.start_date and self.end_date:
            domain.extend([('project_start_date', '>=', self.start_date), ('project_end_date', '<=', self.end_date)])
        elif not self.project_ids.ids and self.start_date and not self.end_date:
            domain.append(('project_start_date', '>=', self.start_date))
        elif not self.project_ids.ids and not self.start_date and self.end_date:
            domain.append(('project_end_date', '<=', self.end_date))
        project_ids = self.env['project.project'].search(domain).ids
        data = {
            'wizard_data': project_ids,
        }
        return self.env.ref('sharq_expense.action_monthly_expense_report').report_action(self, data=data)

