# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SharqProduct(models.Model):
    _name = 'sharq.product'
    _description = 'sharq.product'


    name = fields.Char('Name', index=True, required=True)
    price = fields.Float('Price', required=True)
    image = fields.Binary(" ")
    barcode = fields.Char('Barcode')

    # taxes_id = fields.Many2many('account.tax', 'sharq_product_taxes_rel', 'prod_id', 'tax_id', help="Default taxes used when selling the product.", string='Customer Taxes',
    #     domain=[('type_tax_use', '=', 'sale')], default=lambda self: self.env.company.account_sale_tax_id)
    # supplier_taxes_id = fields.Many2many('account.tax', 'sharq_product_supplier_taxes_rel', 'prod_id', 'tax_id', string='Vendor Taxes', help='Default taxes used when buying the product.',
    #     domain=[('type_tax_use', '=', 'purchase')], default=lambda self: self.env.company.account_purchase_tax_id)
