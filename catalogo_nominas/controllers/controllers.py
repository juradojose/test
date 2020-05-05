# -*- coding: utf-8 -*-
from odoo import http

# class CatalogoNominas(http.Controller):
#     @http.route('/catalogo_nominas/catalogo_nominas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/catalogo_nominas/catalogo_nominas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('catalogo_nominas.listing', {
#             'root': '/catalogo_nominas/catalogo_nominas',
#             'objects': http.request.env['catalogo_nominas.catalogo_nominas'].search([]),
#         })

#     @http.route('/catalogo_nominas/catalogo_nominas/objects/<model("catalogo_nominas.catalogo_nominas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('catalogo_nominas.object', {
#             'object': obj
#         })