# -*- coding: utf-8 -*-
{
    'name': "escuela_module",

    'summary': "Control escolar",

    'description': "Sistema para control escolar",

    'author': "DariuzcmCO",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/Alumnos.xml',
        'views/Maestros.xml',
        'views/Calificaciones.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    'installable':True,
    'autoinstallable':False,
    'application':True
}