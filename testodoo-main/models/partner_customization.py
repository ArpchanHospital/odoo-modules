# -*- coding: utf-8 -*-
from odoo import models,osv, fields, api, _
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError
class PartnerCustomization(models.Model):
    _inherit = 'res.partner'
    is_supplier = fields.Boolean('Is Supplier?')
    supplier_category = fields.Many2one('supplier.classification','Supplier Category', store=True)
    bank_name=fields.Char('Bank Name')
    Branch_name=fields.Char('Branch Name')
    bank_ac_num=fields.Char('Bank Account Number')