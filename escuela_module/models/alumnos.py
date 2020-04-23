# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
class partner_inherit(models.Model):
    _inherit=['res.partner']

    direccion_2=fields.Char( string='Direccion alternativa')

class EscuelaAlumno(models.Model):
    _name="escuela_module.escuela_alumno"
    _rec_name='matricula'
    #_inherit=['mail.thread','mail.tracking.value']

    imagen=fields.Binary('Fotografía')
    nombre= fields.Char(string="Nombre" )
    apellido_pat=fields.Char(string="Apellido Paterno")
    apellido_mat=fields.Char(string="Apellido Materno")
    fecha_ingreso=fields.Date(string="Fecha de Ingreso", default= lambda self: fields.datetime.now())
    
    activo= fields.Selection([
        ('activo' , 'Activo'),
        ('inactivo','Inactivo')
    ],string="Activo")

    promedio_acumulado= fields.Float(string="Promedio Acumulado", digits=(3,2))
    direccion=fields.Char(string="Dirección" )
    matricula=fields.Char(string="Matricula", required=True, copy=False, readonly=True,
                   index=True, default=lambda self: _('New'))

    grupo=fields.Many2one('escuela_module.escuela_grupos','Grupo de Alumno')
    materias= fields.Many2many('escuela_module.materias',string="Materias Asignadas")
    @api.model
    def create(self, vals):
        vals['matricula'] = self.env['ir.sequence'].next_by_code('generate_matricula') or _('New')
        res = super(EscuelaAlumno, self).create(vals)
        return res