# -*- coding: utf-8 -*-
from odoo import http

# class CatalogosGenerales(http.Controller):
#     @http.route('/catalogos_generales/catalogos_generales/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/catalogos_generales/catalogos_generales/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('catalogos_generales.listing', {
#             'root': '/catalogos_generales/catalogos_generales',
#             'objects': http.request.env['catalogos_generales.catalogos_generales'].search([]),
#         })

#     @http.route('/catalogos_generales/catalogos_generales/objects/<model("catalogos_generales.catalogos_generales"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('catalogos_generales.object', {
#             'object': obj
#         })