# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class nuevo_modulo_capacitacion(models.Model):
#     _name = 'nuevo_modulo_capacitacion.nuevo_modulo_capacitacion'
#     _description = 'nuevo_modulo_capacitacion.nuevo_modulo_capacitacion'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
