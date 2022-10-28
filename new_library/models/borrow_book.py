import logging
from odoo import models, fields
_logger = logging.getLogger(__name__)


class BorrowBook(models.Model):
    _name = 'new.lib.borrow.book'
    _description = 'Borrow Book'
    date = fields.Date()
    client_id = fields.Many2one(
        comodel_name='new.lib.client',
        ondelete='cascade',)
    book_ids = fields.Many2many(
        comodel_name='new.lib.book',
        ondelete='cascade', )
    active = fields.Boolean(default=True,)
