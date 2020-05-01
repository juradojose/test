# -*- coding: utf-8 -*-
from odoo import http

# class RhNominas(http.Controller):
#     @http.route('/rh_nominas/rh_nominas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rh_nominas/rh_nominas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rh_nominas.listing', {
#             'root': '/rh_nominas/rh_nominas',
#             'objects': http.request.env['rh_nominas.rh_nominas'].search([]),
#         })

#     @http.route('/rh_nominas/rh_nominas/objects/<model("rh_nominas.rh_nominas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rh_nominas.object', {
#             'object': obj
#         })