# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta
import random
import string


#Modulo Gym de la segunda semana de capacitación Systeg
class modulogym_inheritance(models.Model):
    _inherit = 'res.partner'

    contacto_emergencia = fields.Char(string="Contacto de Emergencia")

class modulogym(models.Model):
    _name = 'modulogym.modulogym'
    _rec_name = 'nombre_socio' 

    @api.model
    def create(self, values):
     	cr = super(modulogym, self).create(values)
     	cr['override_create']=True
     	print 'Función Override Create funciona! valor: ' + str(cr['override_create'])
     	return cr   

    @api.multi
    def write(self, values):
     	values['override_write']="Esta vacio"
     	wr = super(modulogym, self).write(values)
     	print 'Función Override Write funciona!' #' valor: '  + str(wr['override_write'])
     	return wr

    @api.multi
    def unlink(self):			
     	print 'Función Override Unlink funciona!'
     	return super(modulogym, self).unlink()		
     	

    nombre_socio = fields.Char(string="Nombre Socio", required="true")
    direccion_socio = fields.Text(string="Domicilio Socio", required="true")
    telefono_socio = fields.Char(string="Número celular Socio", required="true")
    edad_socio = fields.Integer(string="Edad Socio", required="true")
    inscripcion_socio = fields.Date(string="Fecha Inscripción", default= lambda self:fields.datetime.now())
    sexo_socio = fields.Selection([('h', 'Hombre'),('m', 'Mujer')],string="Sexo del Socio", required="true")
    metodo_pago = fields.Selection([('TDC', 'Tarjeta de Crédito'),('$', 'Efectivo')],string="Método de Pago")
    imagen = fields.Binary(string="Fotografia", attachment=True)
    override_create = fields.Boolean(string="Función Override Create", readonly=True)
    override_write = fields.Char(string="Función Override Write")
    pago = fields.Char(string="Pago Socio", readonly=True)
class modulogymstaff(models.Model):
	_name = 'modulogymstaff.modulogymstaff'
	_rec_name = 'nombre_staff'

	def confirmar_progressbar(self):
		for rec in self:
			rec.state = 'c'


	def listo_progressbar(self):
		for rec in self:
			rec.state = 'l'

	#This function is triggered when the user clicks on the button 'In progress'
	@api.one
	def progress_progressbar(self):
		self.write({
		'state': 'instructor'
		})

	nombre_staff = fields.Char(string="Nombre Staff", required="true")
	direccion_staff = fields.Text(string="Domicilio Staff", required="true")
	telefono_staff = fields.Char(string="Número celular Staff", required="true")
	ingreso_staff = fields.Date(string="Fecha Inscripción", default= lambda self:fields.datetime.now())
	sexo_staff = fields.Selection([('h', 'Hombre'),('m', ('Mujer'))], required="true")
	puesto_staff = fields.Selection([('i', 'Instructor'),('a', 'Administrativo')],string="Puesto Staff")
	email_staff = fields.Char(string="Email", required="true")
	imagen = fields.Binary(string="Fotografia", attachment=True)
	state = fields.Selection([
	('b', 'Borrador'),
	('c', 'Confirmar'),
	('l', 'Listo'),
	],default='b')

class modulogymins(models.Model):
    _name = 'modulogymins.modulogymins'
    _rec_name = 'socio'
    
    @api.one
    def confirmar(self):
        self.write({'asistencia': 'Asistencia Confirmada'})
    
    clase = fields.Many2one("modulogymclases.modulogymclases", string="Nombre de la Clase")
    socio = fields.Many2one("modulogym.modulogym", string="Nombre del Socio")
    observaciones = fields.Char("Observaciones del Socio")
    seccion = fields.Selection([('Zumba', 'Zumba'),('Body-Combat', 'Body Combat'),('Pesas', 'Pesas'),('Kick-Boxing', ('Kick-Boxing'))])
    asistencia = fields.Char(string="Asistencia Confirmada", readonly=True)


class modulogymclases(models.Model):
	_name = 'modulogymclases.modulogymclases'
	_rec_name = 'nombre_clase'

	


	@api.one
	def genera_1(self):
		letras = string.ascii_lowercase
		self.write({'primer_c': ''.join(random.choice(letras) for i in range(8))})

	@api.one	
	def limpiar(self):
		self.write({'primer_c': '', 'segundo_c': '', 'tercer_c': ''})	
	
	@api.one
	def campo_comp(self):
		self.clave_clase = self.primer_c

	nombre_clase = fields.Char(string="Nombre Clase")
	horario_clase = fields.Char(string="Hora de Clase")
	instructor_clase = fields.Many2one("modulogymstaff.modulogymstaff", string="Instructor de la Clase")
	clave_clase = fields.Char(compute="campo_comp", string="Clave de la Clase", readonly=True)
	primer_c = fields.Char(string="Caracteres Generados Aleotoriamente", readonly=True)
	terminada = fields.Char(string="Clase Terminada", readonly=True)
"""class modulogymins(models.Model):
	 _name ='modulogymins.modulogymins'
	 _rec_name = 'ins_socio'

	 ins_clase = fields.Many2one("modulogymclases.modulogymclases", string="Nombre de la Clase")	
	 ins_socio = fields.Many2one("modulogym.modulogym", string="Nombre del socio")
	 ins_seccion = fields.Selection([('z', 'Salón Zumba'),('t', 'Zona TRX'),('p', 'Zona Pesas'),('b', 'Salón Body Combat')],string="Zona/Salón ")
	 ins_observaciones_socio = fields.Char(string="Observaciones del socio")
	 ins_confirmada = fields.char(string="Clase confirmada", readonly=True)"""
