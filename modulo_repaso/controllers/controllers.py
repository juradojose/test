# -*- coding: utf-8 -*-
from odoo import http

# class ModuloRepaso(http.Controller):
#     @http.route('/modulo_repaso/modulo_repaso/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_repaso/modulo_repaso/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_repaso.listing', {
#             'root': '/modulo_repaso/modulo_repaso',
#             'objects': http.request.env['modulo_repaso.modulo_repaso'].search([]),
#         })

#     @http.route('/modulo_repaso/modulo_repaso/objects/<model("modulo_repaso.modulo_repaso"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_repaso.object', {
#             'object': obj
#         })