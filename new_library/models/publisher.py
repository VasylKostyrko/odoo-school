import logging
from odoo import models, fields
_logger = logging.getLogger(__name__)


class Publisher(models.Model):
    _name = 'new.lib.publisher'
    _description = 'Publisher'
    _order = 'name'

    name = fields.Char(required=True)
    city = fields.Char()

