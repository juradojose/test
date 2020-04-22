# -*- coding: utf-8 -*-
from odoo import http

# class ExampleStatusbar1(http.Controller):
#     @http.route('/example_statusbar_1/example_statusbar_1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/example_statusbar_1/example_statusbar_1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('example_statusbar_1.listing', {
#             'root': '/example_statusbar_1/example_statusbar_1',
#             'objects': http.request.env['example_statusbar_1.example_statusbar_1'].search([]),
#         })

#     @http.route('/example_statusbar_1/example_statusbar_1/objects/<model("example_statusbar_1.example_statusbar_1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('example_statusbar_1.object', {
#             'object': obj
#         })