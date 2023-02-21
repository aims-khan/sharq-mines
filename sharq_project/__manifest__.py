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

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['web', 'project','hr'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/project_view.xml',
        'views/newproject_view.xml',
        'views/employees_view.xml',

    ],
    'assets': {
        'web.assets_backend': [
            'sharq_project/static/src/js/project_kanban.js',
        ],
    },
    'demo': [
    ],
}
