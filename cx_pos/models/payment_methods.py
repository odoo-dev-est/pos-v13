# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError

class PaymentMethodID(models.Model):
    _inherit = 'pos.payment.method'


    register_id = fields.Integer(string='Register id', default=0)

    @api.constrains('register_id')
    def _check_register_id(self):
        for rec in self:
            register_ids = rec.search_count([('register_id','!=',0)])

            if register_ids >= 24:
                raise UserError("You already have 24 payment methods!")
                
            if rec.register_id < 0 or rec.register_id > 24:
                raise UserError("Please select an integer from 0 to 24!")

    
    _sql_constraints = [
        ('register_id_unique', 'unique(register_id)', 'This id already exists, please  select another one!')
    ]
    
