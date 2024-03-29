# -*- coding: utf-8 -*-
{
    'name': "project",

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
    'depends': ['web', 'project', 'sharq_investment'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/project_view.xml',
        'reports/report.xml',
        'reports/project_record_report.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'sharq_project/static/src/js/project_kanban.js',
        ],
    },
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'license': 'LGPL-3',
}
