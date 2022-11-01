import logging
from odoo import models, fields
_logger = logging.getLogger(__name__)


class Client(models.Model):
    _name = 'new.lib.client'
    _description = 'Client'
    name = fields.Char()
    first_name = fields.Char()
    last_name = fields.Char()
    about = fields.Text()
    birthday = fields.Date()
    borrow_ids = fields.One2many('new.lib.borrow.book', 'client_id', string='Borrow Docs')
    active = fields.Boolean(default=True,)

    def get_full_name(self):
        self.ensure_one()
        return f'{self.first_name} {self.last_name}'
