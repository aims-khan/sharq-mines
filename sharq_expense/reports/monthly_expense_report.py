from odoo import models, api

class MontlyExpenseReportAbstract(models.AbstractModel):
    _name = 'report.sharq_expense.monthly_expense_report'
    _description = 'Monthly Sales Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        print("\n\n\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", data.get('wizard_data'))
        return {
            'data': data.get('wizard_data')
        }