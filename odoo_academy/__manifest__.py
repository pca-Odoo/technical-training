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
    
    'depends': ['base'],
    'data': [
        'security/academy_security.xml',
        'security/academy_groups.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        
    ],
    'demo': [
        'demo/academy_demo.xml',
        
    ],
}