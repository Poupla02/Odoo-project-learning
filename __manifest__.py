# -*- coding: utf-8 -*-
{
    'name' : 'Gestion de commande',
    'version' : '1.0',
    'summary': 'Gérer les commande d\'un restaurant',
    'sequence': -100,
    'description': """
        Gérer les commande d\'un restaurant
    """,
    'category': 'Marketing',
    'website': 'https://www.odoo.com/page/billing',
    'depends':['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}
