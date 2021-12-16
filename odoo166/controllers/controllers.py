# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo166(http.Controller):
#     @http.route('/odoo166/odoo166/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo166/odoo166/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo166.listing', {
#             'root': '/odoo166/odoo166',
#             'objects': http.request.env['odoo166.odoo166'].search([]),
#         })

#     @http.route('/odoo166/odoo166/objects/<model("odoo166.odoo166"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo166.object', {
#             'object': obj
#         })
