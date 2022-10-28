import logging
from odoo import models, fields
_logger = logging.getLogger(__name__)


class ReturnBook(models.Model):
    _name = 'new.lib.return.book'
    _description = 'Return Book'
    date = fields.Date()
    client_id = fields.Many2one(
        comodel_name='new.lib.client',
        ondelete='cascade',)
    book_ids = fields.Many2many(
        comodel_name='new.lib.book',
        ondelete='cascade', )
    active = fields.Boolean(default=True,)
