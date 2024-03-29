# -*- coding: utf-8 -*-
{
    'name': "sharq_expense",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sharq_project'],

    # always loaded
    'data': [
        'security/sharq_expense_security.xml',
        'security/ir.model.access.csv',
        'views/sharq_expense_view.xml',
        'views/sharq_product_view.xml',
        'wizard/sharq_monthly_expense_report_wizard_view.xml',
        'reports/reports.xml',
        'reports/monthly_expense_report.xml',
        'reports/sharq_expense_record_report.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'license': 'LGPL-3',
}
