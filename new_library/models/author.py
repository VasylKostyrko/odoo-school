import logging
from odoo import models, fields
_logger = logging.getLogger(__name__)


class Author(models.Model):
    _name = 'new.lib.author'
    _description = 'Author'
    _order = 'name'

    name = fields.Char(required=True)
    first_name = fields.Char()
    last_name = fields.Char()
    about = fields.Text(translate=True,)
    birth = fields.Char()
    death = fields.Char()
    color = fields.Integer('Color',)
    book_ids = fields.Many2many(
        comodel_name='new.lib.book',
        ondelete='cascade',)
    active = fields.Boolean(default=True,)

    def set_confirm(self):
        pass

    def get_full_name(self):
        self.ensure_one()
        return f'{self.first_name} {self.last_name}'
