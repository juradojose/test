# -*- coding: utf-8 -*-
from odoo import http

# class RhNomina(http.Controller):
#     @http.route('/rh_nomina/rh_nomina/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rh_nomina/rh_nomina/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rh_nomina.listing', {
#             'root': '/rh_nomina/rh_nomina',
#             'objects': http.request.env['rh_nomina.rh_nomina'].search([]),
#         })

#     @http.route('/rh_nomina/rh_nomina/objects/<model("rh_nomina.rh_nomina"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rh_nomina.object', {
#             'object': obj
#         })