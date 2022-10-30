import logging
from odoo import models, fields
_logger = logging.getLogger(__name__)


class Client(models.Model):
    _name = 'new.lib.client'
    _description = 'Client'
    first_name = fields.Char()
    last_name = fields.Char()
    about = fields.Text()
    birthday = fields.Date()
    active = fields.Boolean(default=True,)

    def get_full_name(self):
        self.ensure_one()
        return f'{self.first_name} {self.last_name}'
