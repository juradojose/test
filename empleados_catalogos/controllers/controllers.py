# -*- coding: utf-8 -*-
from odoo import http

# class EmpleadosCatalogos(http.Controller):
#     @http.route('/empleados_catalogos/empleados_catalogos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/empleados_catalogos/empleados_catalogos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('empleados_catalogos.listing', {
#             'root': '/empleados_catalogos/empleados_catalogos',
#             'objects': http.request.env['empleados_catalogos.empleados_catalogos'].search([]),
#         })

#     @http.route('/empleados_catalogos/empleados_catalogos/objects/<model("empleados_catalogos.empleados_catalogos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('empleados_catalogos.object', {
#             'object': obj
#         })