# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
#Añadiendo descripcion en maestros para pull request

class EscuelaMaestro(models.Model):
    _name="escuela_module.maestro"
    _rec_name="nombre"
    
    imagen=fields.Binary('Fotografía')
    nombre= fields.Char(string="Nombre")
    apellido_pat=fields.Char(string="Apellido Paterno")
    apellido_mat=fields.Char(string="Apellido Materno")
    fecha_ingreso=fields.Date(string="Fecha de Ingreso")
    cedula=fields.Char(string="Cedula Profecional")
    activo= fields.Selection([
        ('activo' , 'Activo'),
        ('inactivo','Inactivo')
    ],string="Activo")
    direccion=fields.Char(string="Dirección")
    materias=fields.Many2many('escuela_module.materias',string='Materias Impartidas')
    tutorados=fields.Many2many('escuela_module.escuela_alumno',string='Tutorados')
    state = fields.Selection([
            ('concept', 'Concept'),
            ('started', 'Started'),
            ('progress', 'In progress'),
            ('finished', 'Done'),
            ],default='concept', readonly=True , string='Status')
    #This function is triggered when the user clicks on the button 'Set to concept'
    @api.multi
    def concept_progressbar(self):
	    self.ensure_one()
	    self.write({
	    'state': 'concept',
	    })

    #This function is triggered when the user clicks on the button 'Set to started'
    @api.multi
    def started_progressbar(self):
	    self.ensure_one()
	    self.write({
	       'state': 'started'
	    })

    #This function is triggered when the user clicks on the button 'In progress'
    @api.multi
    def progress_progressbar(self):
	    self.ensure_one()
	    self.write({
    	    'state': 'progress'
	    })

    #This function is triggered when the user clicks on the button 'Done'
    @api.multi
    def done_progressbar(self):
        self.ensure_one()
        self.write({
	        'state': 'finished'
	    })