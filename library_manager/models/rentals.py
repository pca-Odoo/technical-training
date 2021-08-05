# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Rentals(models.Model):
    
    _name = 'library.rental'
    _description = 'Library Rental'
    
    rent_date = fields.Date(string='Date Rented',
                            default=fields.Date.today)
    rent_return = fields.Date(string='Date Returned')
    rent_period = fields.Integer(string='Days Rented',
                                 readonly=True,
                                 compute='_compute_rent_period')
    returned = fields.Boolean(string='Returned',
                              readonly=True,
                              default=False,
                              compute='_compute_returned')
    
    customer_id = fields.Many2one(string='Customer',
                                  required=True,
                                  comodel_name='res.partner')
    
    book_id = fields.Many2one(string='Book',
                              required=True,
                              comodel_name='library.book')
    book_authors = fields.Text(string='Author(s)', compute='_compute_book_authors')
    book_isbn = fields.Char(string='ISBN', compute='_compute_book_isbn')
    
    @api.depends('rent_date', 'rent_return')
    def _compute_rent_period(self):
        for record in self:
            if record.rent_date and record.rent_return:
                record.rent_period = (record.rent_return - record.rent_date).days + 1
            else:
                record.rent_period = None
                
    @api.depends('rent_return')
    def _compute_returned(self):
        for record in self:
            record.returned = True if record.rent_return else False
                
    @api.onchange('book_id')
    def _compute_book_isbn(self):
        self.book_isbn = self.book_id.isbn if self.book_id else None
                
    @api.onchange('book_id')
    def _compute_book_authors(self):
        self.book_authors = self.book_id.authors if self.book_id else None
