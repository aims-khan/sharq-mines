# -*- coding: utf-8 -*-
# from odoo import http


# class SharqSales(http.Controller):
#     @http.route('/sharq_sales/sharq_sales', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sharq_sales/sharq_sales/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sharq_sales.listing', {
#             'root': '/sharq_sales/sharq_sales',
#             'objects': http.request.env['sharq_sales.sharq_sales'].search([]),
#         })

#     @http.route('/sharq_sales/sharq_sales/objects/<model("sharq_sales.sharq_sales"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sharq_sales.object', {
#             'object': obj
#         })
