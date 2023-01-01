from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'new.lib.library.book'
    _inherit = 'new.lib.book'

    date_return = fields.Date('Date to return')


class LibraryBookCategory(models.Model):
    _name = 'new.lib.library.book.category'
    _inherit = 'new.lib.book.category'

    max_borrow_days = fields.Integer('Maximum borrow days', help="For how many days book can be borrowed", default=10)
