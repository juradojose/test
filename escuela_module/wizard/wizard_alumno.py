# -*- coding: utf-8 -*-

from odoo import models,fields,api

class wizard_alumnos(models.TransientModel):
    _name="escuela_module.wizard_alumnos"
    _description="wizard de Alumno"

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

    @api.multi
    def action_report(self):
        vals={
            'carrera':self.carrera,
            'contraction':self.contraction,
            'grado':self.grado,
            'grupo':self.grupo,
            'field_name':self.field_name
        }
        self.env['escuela_module.escuela_grupos'].create(vals)   
    