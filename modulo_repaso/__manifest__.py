# -*- coding: utf-8 -*-
{
    'name': "ModuloRepaso",

    'summary': "Modulo para realizar un repaso de los puntos aprendidos durante la capacitación",

    'author': "SYSTEG",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
       #'wizard/wizard_ticket.xml',
        'report/report.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'autoinstallable':True,
    'application':True
}