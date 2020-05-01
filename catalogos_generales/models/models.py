# -*- coding: utf-8 -*-

from odoo import models, fields, api
class selectable_catalogos(models.Model):
    _name="cat_general.selectable"

    fecha_inicial = fields.Date(string="Fecha Inicial")
    fecha_fin = fields.Date(string="Fecha Final")
    dependencia = fields.Many2one('catalogos.dependencia',string="Dependencia",required=True, readonly=True)
    subdependencia = fields.Many2one('catalogos.subdependencia',string="Subdependencia")
    direccion = fields.Many2one('catalogos.direccion',string="Coordinación general/Dirección general")
    dir_area = fields.Many2one('catalogos.dir_area',string='Dirección de área')
    jerarquia = fields.Selection(selection=[
        ('dependencia','Dependencia'),
        ('subdependencia','Sub-Dependencia'),
        ('direccion','Coord. Genereal/Dirección general'),
        ('dir_area','Dirección Área')
    ])
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
 