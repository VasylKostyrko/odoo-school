import logging
from odoo import api, models, fields
_logger = logging.getLogger(__name__)


class Client(models.Model):
    _name = 'new.lib.client'
    _description = 'Library Member'
    _order = 'name'

    name = fields.Char()    # required="set_full_name", compute=True, store=True, readonly=True)
    first_name = fields.Char()
    last_name = fields.Char()
    about = fields.Text()
    birthday = fields.Date()
    # borrow_ids = fields.One2many('new.lib.borrow.book', 'client_id', string='Borrow Docs')
    active = fields.Boolean(default=True,)

    # @api.depends('first_name', 'second_name')
    @api.onchange('first_name', 'last_name')
    def set_full_name(self):
        # self.ensure_one()
        self.name = f'{self.first_name} {self.last_name}'
        # return f'{self.first_name} {self.last_name}'
