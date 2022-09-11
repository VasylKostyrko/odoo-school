# -*- coding: utf-8 -*-
import logging
from odoo import models, fields             # , api, exceptions, _
_logger = logging.getLogger(__name__)


class Book(models.Model):
    _name = 'kw.lib.book'
    _description = 'Book'
    name = fields.Char()
    active = fields.Boolean(default=True,)
    isbn = fields.Char()
