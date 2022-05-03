# -*- coding: utf-8 -*-
from datetime import date, timedelta, datetime

from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError

class PrintZReport(models.Model):
    _inherit = 'pos.session'

    DATE_SELECTION = [
        ('si','Si'),
        ('no','No')
    ]

    NUMBER_SELECTION = [
        ('si','Si'),
        ('no','No')
    ]

    MODE = [
        ('a','A'),
        ('s','S'),
        ('m','M')
    ]

    z_report_per_date = fields.Selection(DATE_SELECTION, 
                                        string = 'Per Date',
                                        default='si')
    z_report_per_number = fields.Selection(NUMBER_SELECTION,
                                        string='Per Number',
                                        default='no')
    z_report_start_date =fields.Date(string='Start Time',
                            required = True,
                            default=date.today().strftime('%Y-%m-%d'))
                            
    z_report_end_date =fields.Date(string='Finish Time',
                          required=True,
                          default=date.today().strftime('%Y-%m-%d'))

    z_report_start_number = fields.Integer(string="start number", default=0)
    z_report_end_number = fields.Integer(string="end number")

    z_report_mode = fields.Selection(MODE, string="mode", default="s")