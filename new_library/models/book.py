import logging
from odoo import models, fields
_logger = logging.getLogger(__name__)


class Book(models.Model):
    _name = 'new.lib.book'
    _description = 'Library_Book'
    name = fields.Char()
    isbn = fields.Char()
    book_description= fields.Text()
    active = fields.Boolean(default=True,)
    author_ids = fields.Many2many(
        comodel_name='new.lib.author', )
