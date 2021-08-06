# -*- coding: utf-8 -*-

from odoo import api, fields, models

class BookCopy(models.Model):
    
    _name = 'library.book.copy'
    _description = 'Book Copy'
    
    _inherits = {'library.book': 'book_id'}
    
    name = fields.Char(string="Internal Reference")
    book_id = fields.Many2one('library.book', required=True, ondelete='cascade')