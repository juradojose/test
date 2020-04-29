# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class EscuelaGrupos(models.Model):
    _name="escuela_module.escuela_grupos"
    _rec_name='field_name'

    @api.one
    def compute_field(self):
        self.field_name= self.contraction+'-'+ self.grado+self.grupo

    carrera=fields.Char("Nombre de Carrera")
    contraction=fields.Char('Abreviación')
    grado=fields.Selection([
        ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),
        ('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),
        ('11','11')
    ],string="Grado")
    grupo=fields.Selection(
        [
            ('A','A'),
            ('B','B'),
            ('C','C'),
            ('D','D'),
            ('E','E'),
        ], string="Grupo")
    field_name=fields.Char(string="Nombre de Grupo",compute='compute_field')
        
class EscuelaMaterias(models.Model):
    _name="escuela_module.materias"
    _rec_name="clave_materia"

    materia= fields.Char(string="Nombre de materia")
    clave_materia=fields.Char(string="Clave de materia")
    carrera=fields.Many2many('escuela_module.escuela_grupos',string="Carrera")

class EscuelaCalificaciones(models.Model):
    _name="escuela_module.calificaciones"
    _rec_name='materia'
    
    materia=fields.Many2one('escuela_module.materias',string="Materia")
    alumno=fields.Many2one('escuela_module.escuela_alumno',strig="Alumno")
    unidad=fields.Selection([
        ('u1','Unidad 1'),
        ('u2','Unidad 2'),
        ('u3','Unidad 3'),
        ('u4','Unidad 4')
    ],string="Unidad")
    calificacion=fields.Float(string="Calificación",digits=(3,2))
    estatus=fields.Selection([
        (True,'Aprobado'),
        (False,'Reprobado')
    ], readonly=True)
        
    @api.onchange('calificacion')
    def calif_change(self):
        if(self.calificacion> 69.00 ):
            self.estatus=True
        else:
            self.estatus=False
