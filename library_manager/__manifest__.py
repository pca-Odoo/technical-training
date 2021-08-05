# -*- coding: utf-8 -*-

{
    'name': 'Library Manager',
    'summary': """Library app to manage all library needs""",
    'description': """
        Manage all aspects of your library:
        - Books
        - Memberships
        - Rentals
    """,
    
    'author': 'PCA',
    'website': 'https://www.odoo.com',
    'category': 'training',
    'version': '0.1',
    
    'depends': ['base','web_map'],
    'data': [
        'security/library_groups.xml',
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/book_views.xml',
        'views/rental_views.xml',
        'views/library_menuitems.xml',
        
    ],
    'demo': [
        'demo/book_demo.xml',
        
    ],
}