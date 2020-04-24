# -*- coding: utf-8 -*-
# from odoo import http


# class MiModulo3(http.Controller):
#     @http.route('/mi_modulo3/mi_modulo3/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mi_modulo3/mi_modulo3/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mi_modulo3.listing', {
#             'root': '/mi_modulo3/mi_modulo3',
#             'objects': http.request.env['mi_modulo3.mi_modulo3'].search([]),
#         })

#     @http.route('/mi_modulo3/mi_modulo3/objects/<model("mi_modulo3.mi_modulo3"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mi_modulo3.object', {
#             'object': obj
#         })
