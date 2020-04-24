#  compute='crear_id' -*- coding: utf-8 -*-
 # prueba de github para el pull request del axel

from odoo import models, fields, api
class partner_inherit(models.Model):
     _inherit = 'res.partner'
     nombre_padres=fields.Char(string="Papàs herencia")



class prueba_axel(models.Model):
     _name = 'prueba_axel.alumnos'
     _rec_name = 'nombre'

     nombre = fields.Char(string="Nombre del alumno",required=True)
     edad = fields.Integer(string="Edad del alumno", size=3,required=True)
     carrera = fields.Selection([('sistemas','Ing. en sistemas'),('informatica','Ing. en informatica'),('tics','Ing. en TICS')],required=True)
     calif1 = fields.Float(string="Calificaciòn del ceneval",required=True)
     calif2 = fields.Float(string="Calificaciòn del preparatoria",required=True)
     calif3 = fields.Float(string="Calificaciòn del propedeutico",required=True)
     calif = fields.Float(string="Promedio general",readonly=True,required=True)
     materia = fields.Many2one("prueba_axel.maestros",string="materia a elegir")
     facebook = fields.Char(string="Direcciòn de Facebook")
     clave = fields.Char(string="Clave del alumno")
     estado = fields.Boolean(string='Aprobado', compute='_value_pc')
     state = fields.Selection([('aprobados', 'Alumnos aprobados'), ('reprobados', 'Alumnos reprobados')])
     #  def crear_id(self):
     #  self.clave=self.id
     @api.one
     def generar_promedio(self):
          self.calif=(self.calif1+self.calif2+self.calif3)/3

     @api.one
     @api.depends('calif')
     def _value_pc(self):
          if self.calif:
               if self.calif<50.00:
                    self.estado=False
               else:
                    self.estado=True




class prueba_axel(models.Model):
     _name = 'prueba_axel.maestros'
     _rec_name = 'materia'
     nombre = fields.Char(string="Nombre del maestro")
     folio = fields.Integer(string="Folio:", size=3)
     materia = fields.Text(string="materia asignada")
     rfc = fields.Char(string = "RFC", size=13)
     fechanac = fields.Date(string="fecha de nacimiento")
     alumnos = fields.One2many("prueba_axel.alumnos",'materia', string="Alumnos inscritos")
     metodo = fields.Selection([('base','Base'),('inter','Interinato')],default='on')
     state = fields.Selection([('aprobados', 'Alumnos aprobados'), ('reprobados', 'Alumnos reprobados')])

     @api.one
     def alumnos_reprobados (self):
         self.alumnos = self.env['prueba_axel.alumnos'].search([('estado', '=', False)])



"""
     @api.multi
     @api.depends('alumnos')
     def llenarlista(self):
          reg= []
          for rec in self:
               reg.append()"""
