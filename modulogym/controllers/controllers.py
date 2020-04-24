# -*- coding: utf-8 -*-
from odoo import http

# class Modulogym(http.Controller):
#     @http.route('/modulogym/modulogym/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulogym/modulogym/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulogym.listing', {
#             'root': '/modulogym/modulogym',
#             'objects': http.request.env['modulogym.modulogym'].search([]),
#         })

#     @http.route('/modulogym/modulogym/objects/<model("modulogym.modulogym"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulogym.object', {
#             'object': obj
#         })