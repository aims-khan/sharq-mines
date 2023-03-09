# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SharqProduct(models.Model):
    _name = 'sharq.product'
    _description = 'sharq.product'


    name = fields.Char('Name', index=True, required=True)
    price = fields.Float('Price', required=True)
    image = fields.Binary(" ")
    barcode = fields.Char('Barcode')

