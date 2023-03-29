# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SharqProduct(models.Model):
    _name = 'sharq.product'
    _description = 'sharq.product.des'


    name = fields.Char('Name', index=True, required=True)
    image = fields.Binary(" ")
    des = fields.Text("Descripation")
    type=fields.Selection(
        selection=[
            ('oil', "oil"),
            ('machiner', "Minchener"),
            ('misc', 'Misc'),
        ],
        string="Type",
        )
    