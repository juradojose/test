# -*- coding: utf-8 -*-
{
    'name': "Gym",

    'summary': """
        Módulo para inscribir nuevos socios al gym, así como
        instructores.""",

    'description': """
        Inscripciones socios y staff del gym.
    """,

    'author': "Systeg",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report'],

    # always loaded
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'wizards/terminar_clase.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/report.xml',
    ]
}