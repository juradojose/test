# -*- coding: utf-8 -*-
{
    'name': "Modulo Escuela",

    'summary': """
        Este modulo sirve para llevar el control de una escuela
        """,

    'description': """
        En este modulo se llevarà el control de alumnos maestros y materias.
    """,

    'author': "SYSTEG",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','report'],

    # always loaded
    'data': [
        'security/user_groups.xml',
        'views/views.xml',
        'views/report.xml',
        'views/alumno_wizard.xml',
        'security/ir.model.access.csv',

    ],
    # only loaded in demonstration mode

}