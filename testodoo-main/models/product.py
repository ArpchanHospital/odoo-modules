from odoo import api, fields, models, _

from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_round, float_compare
import base64
from datetime import datetime
class Product(models.Model):
    _inherit = 'product.template'


    hsn_number=fields.Char(string="HSN NUmber")