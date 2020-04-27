# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cpago(models.TransientModel):
	_name = "c.pago"

	nombre_socio = fields.Many2one('modulogym.modulogym', string="Nombre Socio")
	pago = fields.Selection([('Si', 'Si'),('No', 'No')],string="¿El socio ya pagó?")

	@api.multi
	def pago_socio(self):
		for record in self:
	 		if record.nombre_socio:
	 			for clave in record.nombre_socio:
	 				clave.pago = self.pago
