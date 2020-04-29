# -*- coding: utf-8 -*-
from odoo import http

# class PruebaAxel(http.Controller):
#     @http.route('/prueba_axel/prueba_axel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prueba_axel/prueba_axel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('prueba_axel.listing', {
#             'root': '/prueba_axel/prueba_axel',
#             'objects': http.request.env['prueba_axel.prueba_axel'].search([]),
#         })

#     @http.route('/prueba_axel/prueba_axel/objects/<model("prueba_axel.prueba_axel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prueba_axel.object', {
#             'object': obj
#         })