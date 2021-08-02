# -*- coding: utf-8 -*-

from odoo import models, fields, api

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
    isbn = fields.Integer(string='ISBN')
    genre = fields.Char(string="Genre", required=True)