# -*- coding: utf-8 -*-
# from odoo import http


# class SharqInvestment(http.Controller):
#     @http.route('/sharq_investment/sharq_investment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sharq_investment/sharq_investment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sharq_investment.listing', {
#             'root': '/sharq_investment/sharq_investment',
#             'objects': http.request.env['sharq_investment.sharq_investment'].search([]),
#         })

#     @http.route('/sharq_investment/sharq_investment/objects/<model("sharq_investment.sharq_investment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sharq_investment.object', {
#             'object': obj
#         })
