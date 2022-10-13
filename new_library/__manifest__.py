{
    "name": "New Library",
    "summary": "Learning Odoo Qweb",

    "author": "Vasyl Kostyrko",
    'website': "https://letu.lviv.ua",

    "category": "Education",
    "version": "15.0.1.0.0",
    "license": "OPL-1",
    "depends": [],
    'external_dependencies': {'python': [], },
    "qweb": [],
    "data": [
        "security/ir.model.access.csv",
        'views/menu.xml',
        'views/book.xml',
        'views/author.xml',
    ],
    'demo': ['data/demo.xml',],
    'installable': True,
    'auto_install': False,
    'images': [
               'static/description/icon.png',
               ],
    'price': 0,
    'currency': 'EUR',
}
