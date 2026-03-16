{
    'name': "Example_website",
    'summary': "Custom Website test for Odoo 18",

    'description': """Pagina Web de ejemplo en Odoo""",

    'author': "Gexito",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '18.0.0.1',
    'aplication': False,

    # any module necessary for this one to work correctly
    'depends': ['base', 'website_sale', 'web'],

    # load de js modules
    'assets': {
        'web.assets_backend': [

        ],
        'web.assets_frontend': [
            'Example_website/static/src/js/owl.iife.js',
            'Example_website/static/src/js/modal_dialog.js',
            'Example_website/static/src/xml/modal_dialog.xml',
            'Example_website/static/src/js/active_modal.js',
        ]
    },

    # always loaded
    'data': [
        'views/templates.xml',
        'views/client_action.xml',
        'views/cart_view.xml',
    ],

    'installable': True,
    'license': 'LGPL-3',
}