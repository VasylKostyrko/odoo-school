import logging
from odoo import api, models, fields
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from odoo.tools.translate import _

_logger = logging.getLogger(__name__)


class Book(models.Model):
    _name = 'new.lib.book'
    _description = 'Book'
    _order = 'name'
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (name)',
         'Помилка: назва книги повинна бути унікальною!'),
        ('page', 'CHECK(pages>0)',
         'Помилка: кількість сторінок книги повнна бути додатньою!')
    ]

    name = fields.Char(required=True)
    isbn = fields.Char()
    publishing = fields.Char()
    year = fields.Integer()
    age = fields.Integer(compute='compute_age', store=True)
    pages = fields.Integer()
    lib_num = fields.Char()
    cost = fields.Float()
    num_item = fields.Integer(default=1,)
    num_available = fields.Integer(default=1,)
    description = fields.Text(translate=True,)
    state = fields.Selection([
        ('draft', 'Unavailable'),
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('lost', 'Lost')],
        'State', default="draft")
    active = fields.Boolean(default=True,)
    author_ids = fields.Many2many(
        comodel_name='new.lib.author',
        ondelete='cascade',)

    @api.depends('year')
    def compute_age(self):
        today = fields.Date.today()
        cur_year = today.year
        for book in self:
            if book.year:
                age = cur_year - book.year
                book.age = age
            else:
                book.age = 0

    @api.constrains('year')
    def _check_year(self):
        for record in self:
            # if record.year and record.year > fields.Date.today().year:
            if record.year > fields.Date.today().year:
                # raise models.ValidationError('Release date must be in the past')
                raise models.ValidationError('Помилка: рік видання книги не може бути більшим від поточного року!')

    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('draft', 'available'),
             ('available', 'borrowed'),
             ('borrowed', 'available'),
             ('available', 'lost'),
             ('borrowed', 'lost'),
             ('lost', 'available')]
        return (old_state, new_state) in allowed

    def change_state(self, new_state):
        for book in self:
            if book.is_allowed_transition(book.state, new_state):
                book.state = new_state
            else:
                msg = _('Moving from %s to %s is not allowed') % (book.state, new_state)
                raise UserError(msg)

    def make_available(self):
        self.change_state('available')

    def make_borrowed(self):
        self.change_state('borrowed')

    def make_lost(self):
        self.change_state('lost')

    # def log_all_library_members(self):
    #     library_member_model = self.env['new.lib.client']
    #     all_members = library_member_model.search([])
    #     print("ALL MEMBERS:")
    #     for member in all_members:
    #         print(member.name)
    #     return True

    def find_book(self):
        domain = [
           ('state', 'ilike', 'Available'),
        ]
        books = self.search(domain)
        for book in books:
            print(book.name)
        return True


