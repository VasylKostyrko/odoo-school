import logging
from odoo import api, models, fields

_logger = logging.getLogger(__name__)


class BookCategory(models.Model):
    _name = 'new.lib.book.category'

    name = fields.Char('Book Category')
    description = fields.Text('Description')
    parent_id = fields.Many2one(
        'new.lib.book.category',
        string='Parent Category',
        ondelete='restrict',
        index=True
    )
    child_ids = fields.One2many(
        'new.lib.book.category', 'parent_id',
        string='Child Categories')

    def create_categories(self):
        category1 = {
            'name': 'Programming Technology',
            'description': 'Programming Technology for Computers'
        }
        category2 = {
            'name': 'Artificial Intelligence',
            'description': 'Methods of Artificial Intelligence'
        }
        parent_category_val = {
            'name': 'Technology',
            'child_ids': [
                (0, 0, category1),
                (0, 0, category2),
            ]
        }
        record = self.env['new.lib.book.category'].create(parent_category_val)
        return True
