import logging
from odoo import models, fields
_logger = logging.getLogger(__name__)


class Book(models.Model):
    _name = 'new.lib.book'
    _description = 'Book'
    name = fields.Char()
    isbn = fields.Char()
    lib_num = fields.Char()
    description = fields.Text()
    active = fields.Boolean(default=True,)
    author_ids = fields.Many2many(
        comodel_name='new.lib.author',
        ondelete='cascade',)
