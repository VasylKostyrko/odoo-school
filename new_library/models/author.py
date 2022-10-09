import logging
from odoo import models, fields
_logger = logging.getLogger(__name__)


class Author(models.Model):
    _name = 'new.lib.author'
    _description = 'Author_of_Book'
    name = fields.Char()
    first_name = fields.Char()
    last_name = fields.Char()
    active = fields.Boolean(default=True, )
