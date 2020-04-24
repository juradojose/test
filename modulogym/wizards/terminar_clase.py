# -*- coding: utf-8 -*-

from odoo import models, fields, api


class terminarclase(models.TransientModel):
	 _name = "terminar.clase"

	 clave_clase = fields.Many2one('modulogymclases.modulogymclases', string="Nombre Clase")
	 terminada = fields.Selection([('SI', 'Si'),('NO', 'No')],string="¿La clase ha terminado?")

	 @api.multi
	 def confirmar_clase(self):
	 	for record in self:
	 		if record.clave_clase:
	 			for clave in record.clave_clase:
	 				clave.terminada = self.terminada

	 

