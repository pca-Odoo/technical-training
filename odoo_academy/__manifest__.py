# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    'summary': """Academy app to manage Training""",
    'description': """
        Academy Module to manage Training:
        - Courses
        - Sessions
        - Attendees
    """,
    
    'author': 'PCA',
    'website': 'https://www.odoo.com',
    'category': 'training',
    'version': '0.1',
    
    'depends': ['sale','contacts'],
    'data': [
        'security/academy_security.xml',
        'security/academy_groups.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml',
        'views/product_views_inherit.xml',
        'wizards/sale_wizard_view.xml',
        
    ],
    'demo': [
        'demo/academy_demo.xml',
        
    ],
}