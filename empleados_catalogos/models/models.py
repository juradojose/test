# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date
import unicodedata

class catalogoDependencia(models.Model):
    _name="catalogos.dependencia"
    _rec_name="dependencia"
    _inherit = 'mail.thread'

    clave= fields.Char(string="Clave", required=True)
    dependencia=fields.Char(string="Dependencia", size=200, required=True)
    nivel=fields.Char(string="Nivel", required=True)
    fecha_inicio=fields.Date(string="Fecha inicio", readonly=True, default= lambda self: fields.datetime.now())
    fecha_fin=fields.Date(string="Fecha fin", readonly=True)

    @api.multi 
    def unlink(self):
        #no se puede borrar si esta vinculado a una subdireccion
        dep = self.dependencia
        subd = self.env['catalogos.subdependencia'].search([('dependencia','=',dep)]).subdependencia
        if not subd:
            return super(catalogoDependencia,self).unlink()
        else:
            print(type(subd))
            message = ''
            if type(subd) == list:
                for subdependency in subd:
                    message += unicodedata.normalize('NFKD',subdependency).encode('ascii','ignore') + ' '
            elif type(subd) == str :
                message = subd
            raise ValidationError('No se puede eliminar dependencia, es usada en : \n' + unicodedata.normalize('NFKD',subd).encode('ascii','ignore'))

class catalogoSubDependencia(models.Model):
    _name="catalogos.subdependencia"
    _rec_name='subdependencia'
    clave=fields.Char(string="Clave", required=True)
    subdependencia=fields.Char(string="Subdependencia", required=True)
    nivel=fields.Char(string='Nivel',required=True)
    dependencia=fields.Many2one("catalogos.dependencia", string="Dependencia")
    fecha_inicio=fields.Date(readonly=True, string="Fecha Inicio",default=lambda self: fields.datetime.now())
    fecha_fin=fields.Date(readonly=True, string="Fecha Fin")


    @api.multi 
    def unlink(self):
    #no se puede borrar si esta vinculado a una dirección
        subdep = self.subdependencia
        direccion = self.env['catalogos.direccion'].search([('subdependencia','=',subdep)]).subdependencia
        if not direccion:
            return super(catalogoSubDependencia,self).unlink()
        else:
            print(type(direccion))
            message = ''
            if type(direccion) == list:
                for direct in direccion:
                    message += unicodedata.normalize('NFKD',direct).encode('ascii','ignore') + ' '
            elif type(direccion) == str :
                message = direccion
            raise ValidationError('No se puede eliminar subdependencia, es usada en : \n' + unicodedata.normalize('NFKD',direccion).encode('ascii','ignore'))


class catalogoDireccion(models.Model): 
    _name="catalogos.direccion"
    _rec_name="direccion"
    
    clave=fields.Char(string="Clave", required=True)
    direccion=fields.Char(string="Coordinación General/Dirección General", required=True)
    nivel=fields.Char(string="Nivel", required=True)
    subdependencia=fields.Many2one('catalogos.subdependencia',string="SubDependencia")
    dependencia=fields.Many2one('catalogos.dependencia',string="Dependencia", required=True)
    fecha_inicio=fields.Date(string="Fecha Inicio", default=lambda self: fields.datetime.now())
    fecha_fin=fields.Date(string='Fecha Fin', default=lambda self: fields.datetime.now())

    @api.multi 
    def unlink(self):
        #no se puede borrar si esta vinculada a una direccion de area
        dirr = self.direccion
        direccion = self.env['catalogos.dir_area'].search([('direccion','=',dirr)]).direccion
        if not direccion:
            return super(catalogoDireccion,self).unlink()
        else:
            print(type(direccion))
            message = ''
            if type(direccion) == list:
                for direct in direccion:
                    message += unicodedata.normalize('NFKD',direct).encode('ascii','ignore') + ' '
            elif type(direccion) == str :
                message = direccion
            raise ValidationError('No se puede eliminar Dirección de area, es usada en : \n' + unicodedata.normalize('NFKD',direccion).encode('ascii','ignore'))


class catalogoDirArea(models.Model):
    _name='catalogos.dir_area'
    _rec_name="dir_area"

    clave = fields.Char(string="Clave", required=True)
    dir_area= fields.Char(string="Dirección de Área", required=True)
    nivel = fields.Char(string="Nivel", required=True)
    direccion= fields.Many2one('catalogos.direccion',string="Coordinación General/Dirección General")
    subdependencia=fields.Many2one('catalogos.subdependencia',string="SubDependencia")
    dependencia=fields.Many2one('catalogos.dependencia',string="Dependencia", required=True)
    fecha_inicio = fields.Date(string="Fecha Inicio", default=lambda self: fields.datetime.now())
    fecha_fin=fields.Date(string='Fecha Fin', default=lambda self: fields.datetime.now())

