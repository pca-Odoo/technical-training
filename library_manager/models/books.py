# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Books(models.Model):
    
    _name = 'library.book'
    _description = 'Book Info'