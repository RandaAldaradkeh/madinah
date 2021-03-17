from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    ma_national_number = fields.Char(string=u'National Number')
    ma_age = fields.Integer(string='Age')
    ma_birth_day = fields.Date(string='BirthDay')
    ma_salary = fields.Char(string=u'Salary')
    ma_diabetes = fields.Boolean(string='Diabetes')
    ma_hypertension = fields.Boolean(string='Hypertension')
    ma_gender = fields.Selection([
        ('male','Male'),
        ('female','Female')
    ])










    _sql_constraints = [
        ('ma_national_number_uniq', 'unique (ma_national_number)', "National Number already exists !"),
    ]



