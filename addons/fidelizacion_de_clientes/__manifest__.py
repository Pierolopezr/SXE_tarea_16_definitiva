# -*- coding: utf-8 -*-
{
    'name': "fidelizacion_de_clientes",

    'summary': "Modulo para saber el grado o nivel de fidelidad del cliente",

    'description': """
Un campo llamdado nivel de fidelidad que se calcule automaticamente.
- Si el contacto tiene codigo de socio: Nivel PREMIUN 
- Si el campo esta vacio: Nivel ESTANDAR
- Si el codigo empieza por G: Nivel GOLD
    """,

    'author': "Piero Lopez",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
