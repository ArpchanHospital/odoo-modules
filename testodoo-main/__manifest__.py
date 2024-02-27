
# -*- coding: utf-8 -*-
{
    'name':'Custom',
    'description':'Custom',
    'author':'Arpchan',
    'website': 'https://www.arpchan.com/',
    'application': True,
    'category': '',
    'version': '0.1',
    'depends': [
        'base',
        'stock',
        'product',
        'purchase',
        'sale',
        'account',
        'board', 
        "mail", 
        "procurement",
        "bahmni_atom_feed",
        "bahmni_stock" ,
        "bahmni_account",
        "stock_account",
        "maintenance"
    ],
    'data': [
       'views/partnerCusotmization.xml',
       'views/product_template.xml',
    ],
}
