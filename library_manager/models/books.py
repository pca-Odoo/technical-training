# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Books(models.Model):
    
    _name = 'library.book'
    _description = 'Book Info'
    
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    
    authors = fields.Text(string='Author(s)',
                          required=True,
                          help='Author of book, can be multiple')
    editors = fields.Text(string='Editor(s)')
    publisher = fields.Char(string='Publisher')
    edition_year = fields.Integer(string='Year of Edition')
    isbn = fields.Char(string='ISBN')
    genre = fields.Char(string="Genre", required=True)
    notes= fields.Text(string='Notes')
    
    @api.onchange('isbn')
    def _onchange_isbn_length(self):
        if self.isbn is not False and len(self.isbn) != 13:
            raise ValidationError("ISBN must be 13 characters long")