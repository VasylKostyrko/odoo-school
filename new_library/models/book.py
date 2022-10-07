import logging
from odoo import models, fields
_logger = logging.getLogger(__name__)


class Book(models.Model):
    _name = 'new.lib.book'
    _description = 'Library Book'
    name = fields.Char()
    active = fields.Boolean(default=True,)
    isbn = fields.Char()
    additional_text = fields.Text()
    author_ids = fields.Many2many(
        comodel_name='new.lib.author', )
