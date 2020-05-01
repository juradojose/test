# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import unicodedata

class rh_sindicato(models.Model):
    _name = 'rh_sin'
    _rec_name = 's_nombre'
    _inherit = 'mail.thread'
    
    s_clave = fields.Char(string="Clave", required="true", track_visibility="always", size=10)
    s_nombre = fields.Char(string="Nombre", size=200, required="true", track_visibility="always")
    fecha_inicio = fields.Date(string="Fecha Inicial", track_visibility="always")
    fecha_final = fields.Date(string="Fecha Final", track_visibility="always")
    status = fields.Selection([('Activo', 'Activo'),('Inactivo', 'Inactivo'),('Baja', 'Baja')],string="Status", track_visibility="always", required="true")
    
    _sql_constraints=[('s_clave_unique', 'unique(s_clave)', 'Esta clave ya está registrada, por favor ingresa otra clave'),('s_nombre_unique', 'unique(s_nombre)', 'Este nombre ya está registrado, por favor ingresa otro nombre')]

class rh_orden(models.Model):
    _name = 'rh_ord'
    _rec_name = 'o_nombre'
    _inherit = 'mail.thread'
    
    o_clave = fields.Char(string="Clave", required="true", track_visibility="always", size=10)
    o_nombre = fields.Char(string="Nombre", size=200, required="true", track_visibility="always")
    fecha_inicio = fields.Date(string="Fecha Inicial", track_visibility="always")
    fecha_final = fields.Date(string="Fecha Final", track_visibility="always")
    

class rh_centrocostos(models.Model):
    _name = 'rh_cost'
    _rec_name = 'c_nombre'
    _inherit = 'mail.thread'
    
    c_clave = fields.Char(string="Clave", required="true", track_visibility="always", size=10)
    c_nombre = fields.Char(string="Nombre", size=200, required="true", track_visibility="always")
    fecha_inicio = fields.Date(string="Fecha Inicial", track_visibility="always")
    fecha_final = fields.Date(string="Fecha Final", track_visibility="always")
    dependencia = fields.Many2one("rh_nominas.rh_nominas", string="Dependencia", required="true", track_visibility="always")
    cd = fields.Char(string="Clave", readonly=True, track_visibility="always")
    subdependencia = fields.Many2one("rh_subdep", string="Subdependencia", track_visibility="always")
    cs = fields.Char(string="Clave", readonly=True, track_visibility="always")
    coord = fields.Many2one("rh_coord", string="Coordinación General", track_visibility="always")
    cc = fields.Char(string="Clave", readonly=True, track_visibility="always")
    dire = fields.Many2one("rh_dir", string="Dirección de Área", track_visibility="always")
    cdi = fields.Char(string="Clave", readonly=True, track_visibility="always")
    adgral = fields.Many2one("rh_adsc", string="Ads. General", track_visibility="always")
    ca = fields.Char(string="Clave", readonly=True, track_visibility="always")
    adpar = fields.Many2one("rh_part", string="Ads. Particular", track_visibility="always")
    cp = fields.Char(string="Clave", readonly=True, track_visibility="always")
    resp = fields.Many2one("rh_resp", string="U. Responsable", track_visibility="always")
    cu = fields.Char(string="Clave", readonly=True, track_visibility="always")
    trab = fields.Many2one("rh_trab", string="Centro de Trabajo", track_visibility="always")
    ct = fields.Char(string="Clave", readonly=True, track_visibility="always")
    
    #_sql_constraints=[('c_clave_unique', 'unique(c_clave)', 'Esta clave ya está registrada, por favor ingresa otra clave'),('c_nombre_unique', 'unique(c_nombre)', 'Este nombre ya está registrado, por favor ingresa otro nombre')]

class rh_centrotrabajo(models.Model):
    _name = 'rh_trab'
    _rec_name = 't_nombre'
    _inherit = 'mail.thread'
    
    t_clave = fields.Char(string="Clave", required="true", track_visibility="always", size=10)
    t_nombre = fields.Char(string="Nombre", size=200, required="true", track_visibility="always")
    fecha_inicio = fields.Date(string="Fecha Inicial", track_visibility="always")
    fecha_final = fields.Date(string="Fecha Final", track_visibility="always")
    dependencia = fields.Many2one("rh_nominas.rh_nominas", string="Dependencia", required="true", track_visibility="always")
    cd = fields.Char(string="Clave", readonly=True, track_visibility="always")
    subdependencia = fields.Many2one("rh_subdep", string="Subdependencia", track_visibility="always")
    cs = fields.Char(string="Clave", readonly=True, track_visibility="always")
    coord = fields.Many2one("rh_coord", string="Coordinación General", track_visibility="always")
    cc = fields.Char(string="Clave", readonly=True, track_visibility="always")
    dire = fields.Many2one("rh_dir", string="Dirección de Área", track_visibility="always")
    cdi = fields.Char(string="Clave", readonly=True, track_visibility="always")
    adgral = fields.Many2one("rh_adsc", string="Ads. General", track_visibility="always")
    ca = fields.Char(string="Clave", readonly=True, track_visibility="always")
    adpar = fields.Many2one("rh_part", string="Ads. Particular", track_visibility="always")
    cp = fields.Char(string="Clave", readonly=True, track_visibility="always")
    resp = fields.Many2one("rh_resp", string="U. Responsable", track_visibility="always")
    cu = fields.Char(string="Clave", readonly=True, track_visibility="always")
    
    _sql_constraints=[('t_clave_unique', 'unique(t_clave)', 'Esta clave ya está registrada, por favor ingresa otra clave'),('t_nombre_unique', 'unique(t_nombre)', 'Este nombre ya está registrado, por favor ingresa otro nombre')]

class rh_unidad(models.Model):
    _name = 'rh_resp'
    _rec_name = 'r_nombre'
    _inherit = 'mail.thread'
    
    r_clave = fields.Char(string="Clave", required="true", track_visibility="always", size=10)
    r_nombre = fields.Char(string="Nombre", size=200, required="true", track_visibility="always")
    fecha_inicio = fields.Date(string="Fecha Inicial", track_visibility="always")
    fecha_final = fields.Date(string="Fecha Final", track_visibility="always")
    dependencia = fields.Many2one("rh_nominas.rh_nominas", string="Dependencia", required="true", track_visibility="always")
    cd = fields.Char(string="Clave", readonly=True, track_visibility="always")
    subdependencia = fields.Many2one("rh_subdep", string="Subdependencia", track_visibility="always")
    cs = fields.Char(string="Clave", readonly=True, track_visibility="always")
    coord = fields.Many2one("rh_coord", string="Coordinación General", track_visibility="always")
    cc = fields.Char(string="Clave", readonly=True, track_visibility="always")
    dire = fields.Many2one("rh_dir", string="Dirección de Área", track_visibility="always")
    cdi = fields.Char(string="Clave", readonly=True, track_visibility="always")
    adgral = fields.Many2one("rh_adsc", string="Ads. General", track_visibility="always")
    ca = fields.Char(string="Clave", readonly=True, track_visibility="always")
    adpar = fields.Many2one("rh_part", string="Ads. Particular", track_visibility="always")
    cp = fields.Char(string="Clave", readonly=True, track_visibility="always")
    
    _sql_constraints=[('r_clave_unique', 'unique(r_clave)', 'Esta clave ya está registrada, por favor ingresa otra clave'),('r_nombre_unique', 'unique(r_nombre)', 'Este nombre ya está registrado, por favor ingresa otro nombre')]

class rh_adparticular(models.Model):
    _name = 'rh_part'
    _rec_name = 'p_nombre'
    _inherit = 'mail.thread'
    
    p_clave = fields.Char(string="Clave", required="true", track_visibility="always", size=10)
    p_nombre = fields.Char(string="Nombre", size=200, required="true", track_visibility="always")
    fecha_inicio = fields.Date(string="Fecha Inicial", track_visibility="always")
    fecha_final = fields.Date(string="Fecha Final", track_visibility="always")
    dependencia = fields.Many2one("rh_nominas.rh_nominas", string="Dependencia", required="true", track_visibility="always")
    cd = fields.Char(string="Clave", readonly=True, track_visibility="always")
    subdependencia = fields.Many2one("rh_subdep", string="Subdependencia", track_visibility="always")
    cs = fields.Char(string="Clave", readonly=True, track_visibility="always")
    coord = fields.Many2one("rh_coord", string="Coordinación General", track_visibility="always")
    cc = fields.Char(string="Clave", readonly=True, track_visibility="always")
    dire = fields.Many2one("rh_dir", string="Dirección de Área", track_visibility="always")
    cdi = fields.Char(string="Clave", readonly=True, track_visibility="always")
    adgral = fields.Many2one("rh_adsc", string="Ads. General", track_visibility="always")
    ca = fields.Char(string="Clave", readonly=True, track_visibility="always")
    jerarquia = fields.Selection([('Dependencia', 'Dependencia'),('Subdependencia', 'Subdependencia'),('Coord. General', 'Coord. General'),('Dirección Área', 'Dirección Área')],string="Jerarquía", track_visibility="always")
    
    _sql_constraints=[('p_clave_unique', 'unique(p_clave)', 'Esta clave ya está registrada, por favor ingresa otra clave'),('p_nombre_unique', 'unique(p_nombre)', 'Este nombre ya está registrado, por favor ingresa otro nombre')]
    

class rh_adscripcion(models.Model):
    _name = 'rh_adsc'
    _rec_name = 'ad_nombre'
    _inherit = 'mail.thread'
    
    ad_clave = fields.Char(string="Clave", required="true", track_visibility="always", size=10)
    ad_nombre = fields.Char(string="Nombre", size=200, required="true", track_visibility="always")
    fecha_inicio = fields.Date(string="Fecha Inicial", track_visibility="always")
    fecha_final = fields.Date(string="Fecha Final", track_visibility="always")
    dependencia = fields.Many2one("rh_nominas.rh_nominas", string="Dependencia", required="true", track_visibility="always")
    cd = fields.Char(string="Clave", readonly=True, track_visibility="always")
    subdependencia = fields.Many2one("rh_subdep", string="Subdependencia", track_visibility="always")
    cs = fields.Char(string="Clave", readonly=True, track_visibility="always")
    coord = fields.Many2one("rh_coord", string="Coordinación General", track_visibility="always")
    cc = fields.Char(string="Clave", readonly=True, track_visibility="always")
    dire = fields.Many2one("rh_dir", string="Dirección de Área", track_visibility="always")
    cdi = fields.Char(string="Clave",readonly=True, track_visibility="always")
    jerarquia = fields.Selection([('Dependencia', 'Dependencia'),('Subdependencia', 'Subdependencia'),('Coord. General', 'Coord. General'),('Dirección Área', 'Dirección Área')],string="Jerarquía", track_visibility="always")
    
    _sql_constraints=[('ad_clave_unique', 'unique(ad_clave)', 'Esta clave ya está registrada, por favor ingresa otra clave'),('ad_nombre_unique', 'unique(ad_nombre)', 'Este nombre ya está registrado, por favor ingresa otro nombre')]
    
    

class rh_nominas(models.Model):
    _name = 'rh_nominas.rh_nominas'
    _rec_name = 'nombre_dependencia'
    _inherit = 'mail.thread'
    
    @api.multi
    def unlink(self):
        dep = self.nombre_dependencia
        subd = self.env['rh_subdep'].search([('dependencia', '=', dep)]).nombre_subdep
        if not subd:
            return super(rh_nominas,self).unlink()
        else:
            print(type(subd))
        message = ''
        if type(subd) == list:
            for subdependency in subd:
                message += unicodedata.normalize('NFKD', subdependency).encode('ascii', 'ignore') + ' '
        elif type(subd) == str:
            message = subd
        raise ValidationError('No se puede eliminar la dependencia por qué es usada en \n' + unicodedata.normalize('NFKD', subd).encode('ascii', 'ignore'))
    
    clave_dependencia = fields.Char(string="Clave", required="true", track_visibility="always")
    nombre_dependencia = fields.Char(string="Nombre", size=200, required="true", track_visibility="always")
    nivel_dependencia = fields.Float(string="Nivel", required="true", track_visibility="always")
    fecha_inicio = fields.Date(string="Fecha Inicio", track_visibility="always")
    fecha_final = fields.Date(string="Fecha Final", track_visibility="always")

class rh_dir(models.Model):
    _name = 'rh_dir'
    _rec_name = 'nombre_dir'
    _inherit = 'mail.thread'
    
    clave_dir = fields.Char(string="Clave", required="true", track_visibility="always")
    nombre_dir = fields.Char(string="Nombre", required="true", size=200, track_visibility="always")
    nivel_dir = fields.Float(string="Nivel", required="true", track_visibility="always")
    coord = fields.Many2one("rh_coord", string="Coordinación General", track_visibility="always")
    subdependencia = fields.Many2one("rh_subdep", string="Subdependencia", track_visibility="always")
    dependencia = fields.Many2one("rh_nominas.rh_nominas", string="Dependencia", required="true", track_visibility="always")
    fecha_inicio = fields.Date(string="Fehca Inicio", track_visibility="always")
    fecha_final = fields.Date(string="Fecha Final", track_visibility="always")

class rh_corrd(models.Model):
    _name = 'rh_coord'
    _rec_name = 'nombre_coord'
    _inherit = 'mail.thread'
    
    @api.multi
    def unlink(self):
        coordd = self.nombre_coord
        direc = self.env['rh_dir'].search([('coord', '=', coordd)]).nombre_dir
        if not direc:
            return super(rh_corrd,self).unlink()
        else:
            print(type(direc))
        message = ''
        if type(direc) == list:
            for direction in direc:
                message += unicodedata.normalize('NFKD', direction).encode('ascii', 'ignore') + ' '
        elif type(direc) == str:
            message = direc
        raise ValidationError('No se puede eliminar la coordinación por qué es usada en \n' + unicodedata.normalize('NFKD', direc).encode('ascii', 'ignore'))
    
    clave_coord = fields.Char(string="Clave", required="true", track_visibility="always")
    nombre_coord = fields.Char(string="Nombre", required="true", size=200, track_visibility="always")
    nivel_coord = fields.Float(string="Nivel", required="true", track_visibility="always")
    subdependencia = fields.Many2one("rh_subdep", string="Subdependencia", track_visibility="always")
    dependencia = fields.Many2one("rh_nominas.rh_nominas", string="Dependencia", required="true", track_visibility="always")
    fecha_inicio = fields.Date(string="Fecha Inicio", track_visibility="always")
    fecha_final = fields.Date(string="Fecha Final", track_visibility="always")

class rh_subdep(models.Model):
    _name = 'rh_subdep'
    _rec_name = 'nombre_subdep'
    _inherit = 'mail.thread'
    
    @api.multi
    def unlink(self):
        subd = self.nombre_subdep
        coordi = self.env['rh_coord'].search([('subdependencia', '=', subd)]).nombre_coord
        if not coordi:
            return super(rh_subdep,self).unlink()
        else:
            print(type(coordi))
        message = ''
        if type(coordi) == list:
            for coordination in coordi:
                message += unicodedata.normalize('NFKD', coordination).encode('ascii', 'ignore') + ' '
        elif type(coordi) == str:
            message = coordi
        raise ValidationError('No se puede eliminar la subdependencia por qué es usada en \n' + unicodedata.normalize('NFKD', coordi).encode('ascii', 'ignore'))
    
    clave_subdep = fields.Char(string="Clave", required="true", track_visibility="always")
    nombre_subdep = fields.Char(string="Nombre", required="true", size=200, track_visibility="always")
    nivel_subdep = fields.Float(string="Nivel", required="true", track_visibility="always")
    dependencia = fields.Many2one("rh_nominas.rh_nominas", string="Dependencia", required="true", track_visibility="always")
    fecha_inicio = fields.Date(string="Fecha Inicio", track_visibility="always")
    fecha_final = fields.Date(string="Fecha Final", track_visibility="always")

