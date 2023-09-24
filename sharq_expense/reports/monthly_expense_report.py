from odoo import models, api

class MontlyExpenseReportAbstract(models.AbstractModel):
    _name = 'report.sharq_expense.monthly_expense_report'
    _description = 'Monthly Sales Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        return {
            'data': self.env['project.project'].browse(data.get('wizard_data'))
        }
        