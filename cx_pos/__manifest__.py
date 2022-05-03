# -*- coding: utf-8 -*-
{
    'name': "Customizations POS",
    'description': """

    Customizations for Point of Sale, print receipts using api.

    Colaborador: Jesús David Briceño
    """,
    'author': "ESTELIO",
    'category': 'Point of Sale',
    'version': '13.0.1',
    'depends': ['point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/pos_assets.xml',
        'views/account_tax.xml',
        'views/pos_session.xml',
        'views/payment_methods.xml',
        'views/cashier.xml',
        'views/return.xml',
        'views/header_footer.xml'
    ],
    'qweb':[
        'static/src/xml/pos.xml',
        'static/src/xml/pos_return.xml'
    ],
    'installable': True
}
