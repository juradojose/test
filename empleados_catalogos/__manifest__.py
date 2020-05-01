# -*- coding: utf-8 -*-
{
    'name': "empleados_catalogos",

    'summary': "Sección de configuración en catalogos de dependencias",

    'description': """
        Long description of module's purpose
    """,

    'author': "SYSTEG",
    'website': "http://www.systeg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Empleados',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'mail',
        ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/dependencia.xml',
        'views/dir_area.xml',
        'views/subdependencia.xml',
        'views/direccion.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'autoinstallable':True
}