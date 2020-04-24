# -*- coding: utf-8 -*-
from odoo import http

# class ReWritingMethods(http.Controller):
#     @http.route('/re_writing_methods/re_writing_methods/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/re_writing_methods/re_writing_methods/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('re_writing_methods.listing', {
#             'root': '/re_writing_methods/re_writing_methods',
#             'objects': http.request.env['re_writing_methods.re_writing_methods'].search([]),
#         })

#     @http.route('/re_writing_methods/re_writing_methods/objects/<model("re_writing_methods.re_writing_methods"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('re_writing_methods.object', {
#             'object': obj
#         })