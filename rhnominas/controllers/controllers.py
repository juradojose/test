# -*- coding: utf-8 -*-
# from odoo import http


# class Rhnominas(http.Controller):
#     @http.route('/rhnominas/rhnominas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rhnominas/rhnominas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rhnominas.listing', {
#             'root': '/rhnominas/rhnominas',
#             'objects': http.request.env['rhnominas.rhnominas'].search([]),
#         })

#     @http.route('/rhnominas/rhnominas/objects/<model("rhnominas.rhnominas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rhnominas.object', {
#             'object': obj
#         })
