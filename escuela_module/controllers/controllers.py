# -*- coding: utf-8 -*-
from odoo import http

# class EscuelaModule(http.Controller):
#     @http.route('/escuela_module/escuela_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/escuela_module/escuela_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('escuela_module.listing', {
#             'root': '/escuela_module/escuela_module',
#             'objects': http.request.env['escuela_module.escuela_module'].search([]),
#         })

#     @http.route('/escuela_module/escuela_module/objects/<model("escuela_module.escuela_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('escuela_module.object', {
#             'object': obj
#         })