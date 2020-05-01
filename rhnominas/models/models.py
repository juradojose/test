# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rhnominas(models.Model):
    _name = 'rhnominas.rhnominas'
    _description = 'rhnominas.rhnominas'
    #TRAZABILIDAD
    _inherit = 'mail.thread'
    #_inherit = 'rh.employee'
    _rec_name = "dependencia"

    clave = fields.Char(string="Clave",required=True, track_visibility="always")
    dependencia = fields.Char(string="Dependencia",required=True, track_visibility="always")
    nivel = fields.Float(string="Nivel",required=True, track_visibility="always")
    fecha_ini = fields.Date(string="Fecha de inicio", track_visibility="always")
    fecha_fin = fields.Date(string="Fecha de finalizacion", track_visibility="always")

   
    #ESTE CODIGO ES PARA EVITAR BORRAR UNA DEPENDENCIA QUE YA TIENE REGISTRADAS SUBDEPENDENCIAS
    """@api.depends
    def unlink(self):
        #self.ensure_one()
        dep = self.dependencia
        
        subd = self.env['subdependencias.rhnominas'].search([('dependencia','=',dep)]).subdependencia
        
        if not subd:
            return super(rhnominas,self).unlink()
        else:
            print(type(subd))
            message = ''
            if type(subd) == list:
                for subdependency in subd:
                    message += unicodedata.normalize('NFKD',subdependency).encode('ascii','ignore') + ' '
            elif type(subd)==str:
                message = subd
            raise ValidationError('no se puede elimnar la dependencia')"""
   

class subdependencias(models.Model):
    _name = 'subdependencias.rhnominas'
    _description = 'subdependencias.rhnominas'
    #TRAZABILIDAD
    _inherit = 'mail.thread'

    clave = fields.Char(string="Clave",required=True, track_visibility="always")
    subdependencia = fields.Char(string="Subdependencia",required=True, track_visibility="always")
    nivel = fields.Float(string="nivel",required=True, track_visibility="always")
    dependencia = fields.Many2one("rhnominas.rhnominas",required=True, track_visibility="always")
    fecha_ini = fields.Date(string="Fecha de inicio", track_visibility="always")
    fecha_fin = fields.Date(string="Fecha de finalizacion", track_visibility="always")

    

class coordinacion(models.Model):
    _name = 'coordinacion.rhnominas'
    _description = 'coordinacion.rhnominas'
    #TRAZABILIDAD
    _inherit = 'mail.thread'

    clave = fields.Char(string="Clave",required=True, track_visibility="always")
    coordinacion = fields.Char(string="Coordinacion",required=True, track_visibility="always")
    nivel = fields.Float(string="nivel",required=True, track_visibility="always")
    subdependencia = fields.Char(string="Subdependencia", track_visibility="always")
    dependencia = fields.Char(string="Dependencia",required=True, track_visibility="always")
    fecha_ini = fields.Date(string="Fecha de inicio", track_visibility="always")
    fecha_fin = fields.Date(string="Fecha de finalizacion", track_visibility="always")


class direccion_area(models.Model):
    _name = 'direccion.rhnominas'
    _description = 'direccion.rhnominas'
    #TRAZABILIDAD
    _inherit = 'mail.thread'

    clave = fields.Char(string="Clave",required=True, track_visibility="always")
    direccion_area = fields.Char(string="Direccion de area",required=True, track_visibility="always")
    nivel = fields.Float(string="nivel",required=True, track_visibility="always")
    coordinacion = fields.Char(string="Coordinacion", track_visibility="always")
    subdependencia = fields.Char(string="Subdependencia", track_visibility="always")
    dependencia = fields.Char(string="Dependencia",required=True, track_visibility="always")
    fecha_ini = fields.Date(string="Fecha de inicio", track_visibility="always")
    fecha_fin = fields.Date(string="Fecha de finalizacion", track_visibility="always")


class adscripcion_gral(models.Model):
    _name = 'adscripciongral.rhnominas'
    _description = 'adscripciongral.rhnominas'
    #TRAZABILIDAD
    _inherit = 'mail.thread'

    clave = fields.Char(string="Clave", track_visibility="always")
    nombre_adscripcion_gral = fields.Char(string="Nombre de la adscripcion general", track_visibility="always")
    fecha_ini = fields.Date(track_visibility="always")
    fecha_fin = fields.Date(track_visibility="always")
    #A PARTIR DE AQUI CON CAMPOS DE SELECCION
    dependencia = fields.Many2one("rhnominas.rhnominas",required=True, track_visibility="always")
    subdependencia = fields.Many2one("subdependencias.rhnominas",required=True, track_visibility="always")
    coordinacion = fields.Many2one("coordinacion.rhnominas",required=True, track_visibility="always")
    direccion_area = fields.Many2one("direccion.rhnominas",required=True, track_visibility="always")
    


class adscripcion_particular(models.Model):
    _name = 'adscripcionparti.rhnominas'
    _description = 'adscripcionparti.rhnominas'
    #TRAZABILIDAD
    _inherit = 'mail.thread'

    clave = fields.Char(string="Clave", track_visibility="always")
    nombre_adscripcion_particular = fields.Char(string="Nombre de la adscripcion particular", track_visibility="always")
    fecha_ini = fields.Date(track_visibility="always")
    fecha_fin = fields.Date(track_visibility="always")
    #A PARTIR DE AQUI CON CAMPOS DE SELECCION
    dependencia = fields.Many2one("rhnominas.rhnominas",required=True, track_visibility="always")
    subdependencia = fields.Many2one("subdependencias.rhnominas",required=True, track_visibility="always")
    coordinacion = fields.Many2one("coordinacion.rhnominas",required=True, track_visibility="always")
    direccion_area = fields.Many2one("direccion.rhnominas",required=True, track_visibility="always")
    adscripcion_gral = fields.Many2one("adscripciongral.rhnominas",required=True, track_visibility="always")
    


class unidad_responsable(models.Model):
    _name = 'unidadres.rhnominas'
    _description = 'unidadres.rhnominas'
    #TRAZABILIDAD
    _inherit = 'mail.thread'

    clave = fields.Char(string="Clave", track_visibility="always")
    nombre = fields.Char(string="Nombre de la unidad responsable", track_visibility="always")
    fecha_ini = fields.Date(track_visibility="always")
    fecha_fin = fields.Date(track_visibility="always")
    #A PARTIR DE AQUI INICIA LOS CAMPOS DE SELECCION
    dependencia = fields.Many2one("rhnominas.rhnominas",required=True, track_visibility="always")
    subdependencia = fields.Many2one("subdependencias.rhnominas",required=True, track_visibility="always")
    coordinacion = fields.Many2one("coordinacion.rhnominas",required=True, track_visibility="always")
    direccion_area = fields.Many2one("direccion.rhnominas",required=True, track_visibility="always")
    adscripcion_gral = fields.Many2one("adscripciongral.rhnominas",required=True, track_visibility="always")
    adscripcion_particular = fields.Many2one("adscripcionparti.rhnominas",required=True, track_visibility="always")

class centro_trabajo(models.Model):
    _name = 'centrotrabajo.rhnominas'
    _description = 'centrotrabajo.rhnominas'
    #TRAZABILIDAD
    _inherit = 'mail.thread'

    clave = fields.Char(string="Clave", track_visibility="always")
    nombre = fields.Char(string="Nombre del centro de trabajo", track_visibility="always")
    fecha_ini = fields.Date(track_visibility="always")
    fecha_fin = fields.Char(track_visibility="always")
    #A PARTIR DE AQUI EMPIEZAN LOS CAMPOS DE SELECCION
    Dependencia = fields.Many2one("rhnominas.rhnominas",required=True, track_visibility="always")
    subdependencia = fields.Many2one("subdependencias.rhnominas",required=True, track_visibility="always")
    coordinacion = fields.Many2one("coordinacion.rhnominas",required=True, track_visibility="always")
    direccion_area = fields.Many2one("direccion.rhnominas",required=True, track_visibility="always")
    adscripcion_gral = fields.Many2one("adscripciongral.rhnominas",required=True, track_visibility="always")
    adscripcion_particular = fields.Many2one("adscripcionparti.rhnominas",required=True, track_visibility="always")
    unidad_responsable = fields.Many2one("unidadres.rhnominas",required=True)


class centro_de_costos(models.Model):
    _name = 'centrocostos.rhnominas'
    _description = 'centrocostos.rhnominas'
    #TRAZABILIDAD
    _inherit = 'mail.thread'

    clave = fields.Char(string="Clave", track_visibility="always")
    nombre = fields.Char(string="Nombre del centro de costos", track_visibility="always")
    fecha_ini = fields.Date(track_visibility="always")
    fecha_fin = fields.Date(track_visibility="always")
    #A PARTIR DE AQUI INICIAN LOS CAMPOS DE SELECCION
    dependecia = fields.Many2one("rhnominas.rhnominas",required=True, track_visibility="always")
    subdependencia = fields.Many2one("subdependencias.rhnominas",required=True, track_visibility="always")
    coordinacion = fields.Many2one("coordinacion.rhnominas",required=True, track_visibility="always")
    direccion_area = fields.Many2one("direccion.rhnominas",required=True, track_visibility="always")
    adscripcion_gral = fields.Many2one("adscripciongral.rhnominas",required=True, track_visibility="always")
    adscripcion_particular = fields.Many2one("adscripcionparti.rhnominas",required=True, track_visibility="always")
    unidad_responsable = fields.Many2one("unidadres.rhnominas",required=True, track_visibility="always")
    centro_trabajo = fields.Many2one("centrotrabajo.rhnominas",required=True, track_visibility="always")


class catalogo_orden_jerarquico(models.Model):
    _name = 'ordenj.rhnominas'
    _description = 'ordenj.rhnominas'
    #TRAZABILIDAD
    _inherit = 'mail.thread'

    clave = fields.Char(string="Clave", track_visibility="always")
    jerarquia = fields.Char(string="Jerarquia", track_visibility="always")
    fecha_ini = fields.Date(track_visibility="always") 
    fecha_fin = fields.Date(track_visibility="always")


class sindicatos(models.Model):
    _name = 'sindicatos.rhnominas'
    _description = 'sindicatos.rhnominas'
    #TRAZABILIDAD
    _inherit = 'mail.thread'

    clave_sindicato = fields.Char("Clave del sindicato", track_visibility="always")
    nombre = fields.Char("Nombre del sindicato", track_visibility="always")
    fecha_ini = fields.Date(track_visibility="always")
    fecha_fin = fields.Date(track_visibility="always")

