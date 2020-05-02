# -*- coding: utf-8 -*-

from odoo import models, fields, api
class selectable_catalogos(models.Model):
    _name="cat_general.selectable"

    fecha_inicial = fields.Date(string="Fecha Inicial")
    fecha_fin = fields.Date(string="Fecha Final")
    
    dependencia = fields.Many2one('catalogos.dependencia',string="Dependencia",required=True)
    clave_dep=fields.Char(string="Clave", readonly=True)
    
    subdependencia = fields.Many2one('catalogos.subdependencia',string="Subdependencia")
    clave_sub=fields.Char(string="Clave", readonly=True)
    
    direccion = fields.Many2one('catalogos.direccion',string="Coordinación general/Dirección general")
    clave_dir=fields.Char(string="Clave", readonly=True)
    
    dir_area = fields.Many2one('catalogos.dir_area',string='Dirección de área')
    clave_area=fields.Char(string="Clave", readonly=True)
    
    jerarquia = fields.Many2one('cat_generales.jerarquia', string="Jerarquia")
    clave_jer=fields.Char(string="Clave", readonly=True)
    
    @api.onchange('dependencia')
    def changing_key_dep(self):
        dep = self.dependencia
        if dep:
            clave = self.env['catalogos.dependencia'].search([('dependencia','=',dep)]).clave
            self.clave_dep = clave
    @api.onchange('subdependencia')
    def changing_key_subd(self):
        subd = self.subdependencia
        if subd:
            clave = self.env['catalogos.subdependencia'].search([('subdependencia','=',subd)]).clave
            self.clave_sub = clave
    @api.onchange('direccion')
    def changing_key_dir(self):
        direccion = self.direccion
        if direccion:
            clave = self.env['catalogos.direccion'].search([('direccion','=',direccion)]).clave
            self.clave_dir = clave
    @api.onchange('dir_area')
    def changing_key_area(self):
        dir_area = self.dir_area
        if dir_area:
            clave = self.env['catalogos.dir_area'].search([('dir_area','=',dir_area)]).clave
            self.clave_area = clave
    @api.onchange('jerarquia')
    def changing_key_area(self):
        jerarquia = self.jerarquia
        if jerarquia:
            clave = self.env['catalogos.jerarquia'].search([('jerarquia','=',jerarquia)]).clave
            self.clave_jer = clave
class car_generales_jerarquia(models.Model):
    _name="cat_generales.jerarquia"
    
    clave = fields.Char(string="Clave")
    jerarquia = fields.Char(string="Jerarquia")
    fecha_inicio = fields.Char(string="Fecha inicio")
    fecha_final = fields.Char(string="Fecha final")

class cat_generales_Adscripciones(models.Model):
    _name="cat_generales.adscripciones"
    _inherit= ['mail.thread','cat_general.selectable']

    clave = fields.Char(string="Clave", size=10, required=True)
    nombre_ads = fields.Char(string="Nombre de Adscripción", required=True, size=200)
    
class cat_generales_adscripcion_particular(models.Model):
    _name="cat_generales.adscripciones_par"
    _inherit= ['mail.thread','cat_general.selectable']
    
    clave = fields.Char(string="Clave", size=10, required=True)
    nombre_ads_par=fields.Char(string="Nombre Adscripción Particular", size=200,required=True)
    nombre_ads = fields.Many2one('cat_generales.adscripciones',string="Adscripción General")    
  
class cat_generales_Unidad(models.Model):
    _name="cat_generales.unidad"
    _inherit= ['mail.thread','cat_general.selectable']
    
    clave = fields.Char(string="Clave", size=10, required=True)
    nombre_unidad=fields.Char(string="Nombre de la unidad responsable",size=200, required=True)
    nombre_ads = fields.Many2one('cat_generales.adscripciones',string="Adscripción General")    
    nombre_ads_par=fields.Many2one('cat_generales.adscripciones_par',string="Adscripción Particular", size=200,required=True)
 