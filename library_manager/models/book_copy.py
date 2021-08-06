# -*- coding: utf-8 -*-

from odoo import api, fields, models

class BookCopy(models.Model):
    
    _name = 'library.book.copy'
    _description = 'Book Copy'
    
    _inherits = {'library.book': 'book_id'}
    
    name = fields.Char(string="Book Copy",
                       compute="_compute_book_copy_name",
                       store=True)
    reference = fields.Char(string="Internal Reference", required=True)
    book_id = fields.Many2one('library.book', required=True, ondelete='cascade')
    
    @api.depends('reference', 'book_id')
    def _compute_book_copy_name(self):
        for record in self:
            record.name = "[" + record.reference + "] " + record.book_id.name