# -*- coding: utf-8 -*-
{
    'name': "ERS-RH2 Catálogos Base para R.H-Nóminas",

    'summary': """
        Estructura base de
        los   módulos   de   Recursos   Humanos   y   Nóminas,   que   permite   tener   el
        organigrama a detalle conformada por medio de Niveles que ayudan a la
        clasificación del Municipio.""",

    'description': """
        Contar con una   estructura base creada mediante catálogos y campos
        nuevos necesarios para cumplir con la funcionalidad que requieren los
        módulos de Recursos Humanos y Nóminas. 
    """,

    'author': "Systeg",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}