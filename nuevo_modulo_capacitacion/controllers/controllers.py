# -*- coding: utf-8 -*-
# from odoo import http


# class NuevoModuloCapacitacion(http.Controller):
#     @http.route('/nuevo_modulo_capacitacion/nuevo_modulo_capacitacion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nuevo_modulo_capacitacion/nuevo_modulo_capacitacion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nuevo_modulo_capacitacion.listing', {
#             'root': '/nuevo_modulo_capacitacion/nuevo_modulo_capacitacion',
#             'objects': http.request.env['nuevo_modulo_capacitacion.nuevo_modulo_capacitacion'].search([]),
#         })

#     @http.route('/nuevo_modulo_capacitacion/nuevo_modulo_capacitacion/objects/<model("nuevo_modulo_capacitacion.nuevo_modulo_capacitacion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nuevo_modulo_capacitacion.object', {
#             'object': obj
#         })
