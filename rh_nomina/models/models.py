# -*- coding: utf-8 -*-

from odoo import models, fields, api
import unicodedata
#import unicode

from odoo.exceptions import ValidationError


class rh_nominaD(models.Model):
     _inherit = 'mail.thread'
     #_inherit = 'hr.employee'
     _name = 'rh_nomina.dependencia'
     _rec_name = 'dependencia'

     clave = fields.Integer('clave',required=True,track_visibility="always")
     dependencia = fields.Char('Dependencia',size=200,required=True,track_visibility="always")
     nivel = fields.Float('Nivel',required=True,track_visibility="always")
     fecha_inicio=fields.Date('fecha inicio',readonly=True,track_visibility="always")
     fecha_final=fields.Date('fecha final',readonly=True,track_visibility="always")

     @api.multi
     def unlink(self):
      dep = self.dependencia
      subd = self.env['rh_nomina.subdependencia'].search([('dependencia', '=', dep)]).subdependencia
      if not subd:
        return super(rh_nominaD, self).unlink()
      else:
       print(type(subd))
      message = ''
      if type(subd) == list:
          for subdependency in subd:
               message += unicodedata.normalize('NFKD', subdependency).encode('ascii', 'ignore') + ' '
      elif type(subd) == str:
          message = subd
      raise ValidationError(
          'no se puede elimnar la dependencia es usada en \n' + unicodedata.normalize('NFKD', subd).encode('ascii',
                                                                                                           'ignore'))

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class rh_nomina(models.Model):
     _inherit = 'mail.thread'
     #_inherit = 'hr.employee'
     _name = 'rh_nomina.subdependencia'
     _rec_name = 'subdependencia'

     clave = fields.Char('clave',required=True,track_visibility="always")
     subdependencia = fields.Char('Subdepedencia',size=200,required=True,track_visibility="always")
     dependencia = fields.Many2one('rh_nomina.dependencia', string="Dependencia", required=True,track_visibility="always")
     nivel = fields.Float('Nivel',required=True,track_visibility="always")
     fecha_inicio=fields.Date('fecha inicio',readonly=False,track_visibility="always")
     fecha_final=fields.Date('fecha final',readonly=False,track_visibility="always")


class rh_nomina(models.Model):
     #_inherit = 'hr.employee'
     _inherit = 'mail.thread'
     _name = 'rh_nomina.coordinacion'
     _rec_name = 'coordinacion'

     clave = fields.Char('clave',required=True,track_visibility="always")
     coordinacion = fields.Char('Coordinacion',size=200,required=True,track_visibility="always")
     nivel = fields.Float('Nivel', required=True,track_visibility="always")
     subdependencia = fields.Many2one('rh_nomina.subdependencia', string="Subdependencia", required=True,track_visibility="always")
     dependencia = fields.Many2one('rh_nomina.dependencia', string="Dependencia", required=True,track_visibility="always")
     fecha_inicio=fields.Date('fecha inicio',readonly=False,track_visibility="always")
     fecha_final=fields.Date('fecha final',readonly=False ,track_visibility="always")


class rh_nomina(models.Model):
     #_inherit = 'hr.employee'
     _inherit = 'mail.thread'
     _name = 'rh_nomina.direccion'
     _rec_name = 'direccion'

     clave = fields.Char('Clave',required=True,track_visibility="always")
     direccion = fields.Char('Direccion de Area',size=200,required=True,track_visibility="always")
     nivel = fields.Float('Nivel', required=True,track_visibility="always")
     coordinacion = fields.Many2one('rh_nomina.coordinacion', string="Coordinacion", required=True,track_visibility="always")
     subdependencia = fields.Many2one('rh_nomina.subdependencia', string="Subdependencia", required=True,track_visibility="always")
     dependencia = fields.Many2one('rh_nomina.dependencia', string="Dependencia", required=True,track_visibility="always")
     fecha_inicio=fields.Date('fecha inicio',readonly=False,track_visibility="always")
     fecha_final=fields.Date('fecha final',readonly=False,track_visibility="always")

class rh_nomina(models.Model):
     #_inherit = 'hr.employee'
    _inherit = 'mail.thread'
    _name = 'rh_nomina.adgeneral'
    _rec_name = 'nombre'

    clave = fields.Char('Clave',required=True,track_visibility="always",size=10)
    nombre = fields.Text('Adscripcion General',size=200,required=True, track_visibility="always")
    direccion = fields.Many2one('rh_nomina.direccion',string='Direccion de Area',size=200,required=True,track_visibility="always")
    coordinacion = fields.Many2one('rh_nomina.coordinacion', string="Coordinacion", required=True,track_visibility="always")
    subdependencia = fields.Many2one('rh_nomina.subdependencia', string="Subdependencia", required=True,track_visibility="always")
    dependencia = fields.Many2one('rh_nomina.dependencia', string="Dependencia", required=True,track_visibility="always")
    fecha_inicio=fields.Date('fecha inicio',readonly=False,track_visibility="always")
    fecha_final=fields.Date('fecha final',readonly=False,track_visibility="always")
    jerarquia = fields.Selection([('dependencia','Dependencia'),('subdependencia','Sub-dependencia'),('coordinacion','Coordinacion general/Direccion general'),('direccion','Direccion de Area')],required=True)

    _sql_constraints = [('ad_clave_unique','unique(clave)','Clave repetida')]
    @api.depends('dependencia')
    def generar(self):
        print('')


class rh_nomina(models.Model):
    # _inherit = 'hr.employee'
    _inherit = 'mail.thread'
    _name = 'rh_nomina.adparticular'
    _rec_name = 'nombre'

    clave = fields.Char('Clave', required=True, track_visibility="always", size=10)
    nombre = fields.Text('Adscripcion particular', size=200, required=True, track_visibility="always")
    direccion = fields.Many2one('rh_nomina.direccion', string='Direccion de Area', size=200, required=True,
                                track_visibility="always")
    coordinacion = fields.Many2one('rh_nomina.coordinacion', string="Coordinacion", required=True,
                                   track_visibility="always")
    subdependencia = fields.Many2one('rh_nomina.subdependencia', string="Subdependencia", required=True,
                                     track_visibility="always")
    dependencia = fields.Many2one('rh_nomina.dependencia', string="Dependencia", required=True,
                                  track_visibility="always")
    fecha_inicio = fields.Date('fecha inicio', readonly=False, track_visibility="always")
    fecha_final = fields.Date('fecha final', readonly=False, track_visibility="always")
    ad_general = fields.Many2one('rh_nomina.adgeneral',string="Adscripcion General",track_visibility="always")
    jerarquia = fields.Selection([('dependencia', 'Dependencia'), ('subdependencia', 'Sub-dependencia'),
                                ('coordinacion', 'Coordinacion general/Direccion general'),
                                ('direccion', 'Direccion de Area')], required=True,track_visibility="always")
    _sql_constraints = [('ad_clave_unique', 'unique(clave)', 'Clave repetida')]

    @api.depends('dependencia')
    def generar(self):
        print('')

class rh_nomina(models.Model):
    # _inherit = 'hr.employee'
    _inherit = 'mail.thread'
    _name = 'rh_nomina.unidad'
    _rec_name = 'nombre'

    clave = fields.Char('Clave', required=True, track_visibility="always", size=10)
    nombre = fields.Text('Unidad Responsable', size=200, required=True, track_visibility="always")
    direccion = fields.Many2one('rh_nomina.direccion', string='Direccion de Area', size=200, required=True,
                                track_visibility="always")
    coordinacion = fields.Many2one('rh_nomina.coordinacion', string="Coordinacion", required=True,
                                   track_visibility="always")
    subdependencia = fields.Many2one('rh_nomina.subdependencia', string="Subdependencia", required=True,
                                     track_visibility="always")
    dependencia = fields.Many2one('rh_nomina.dependencia', string="Dependencia", required=True,
                                  track_visibility="always")
    fecha_inicio = fields.Date('fecha inicio', readonly=False, track_visibility="always")
    fecha_final = fields.Date('fecha final', readonly=False, track_visibility="always")
    ad_general = fields.Many2one('rh_nomina.adgeneral',string="Adscripcion General",track_visibility="always")
    ad_particular = fields.Many2one('rh_nomina.adparticular', string="Adscripcion Particular", track_visibility="always")
    jerarquia = fields.Selection([('dependencia', 'Dependencia'), ('subdependencia', 'Sub-dependencia'),
                                ('coordinacion', 'Coordinacion general/Direccion general'),
                                ('direccion', 'Direccion de Area')], required=True,track_visibility="always")
    _sql_constraints = [('ad_clave_unique', 'unique(clave)', 'Clave repetida')]

    @api.depends('dependencia')
    def generar(self):
        print('')

class rh_nomina(models.Model):
    # _inherit = 'hr.employee'
    _inherit = 'mail.thread'
    _name = 'rh_nomina.centrot'
    _rec_name = 'nombre'

    clave = fields.Char('Clave', required=True, track_visibility="always", size=10)
    nombre = fields.Text('Centro de trabajo', size=200, required=True, track_visibility="always")
    direccion = fields.Many2one('rh_nomina.direccion', string='Direccion de Area', size=200, required=True,
                                track_visibility="always")
    coordinacion = fields.Many2one('rh_nomina.coordinacion', string="Coordinacion", required=True,
                                   track_visibility="always")
    subdependencia = fields.Many2one('rh_nomina.subdependencia', string="Subdependencia", required=True,
                                     track_visibility="always")
    dependencia = fields.Many2one('rh_nomina.dependencia', string="Dependencia", required=True,
                                  track_visibility="always")
    fecha_inicio = fields.Date('fecha inicio', readonly=False, track_visibility="always")
    fecha_final = fields.Date('fecha final', readonly=False, track_visibility="always")
    ad_general = fields.Many2one('rh_nomina.adgeneral',string="Adscripcion General",track_visibility="always")
    ad_particular = fields.Many2one('rh_nomina.adparticular', string="Adscripcion Particular", track_visibility="always")
    unidad = fields.Many2one('rh_nomina.unidad', string="Unidad responsable", track_visibility="always")

    _sql_constraints = [('ad_clave_unique', 'unique(clave)', 'Clave repetida')]

    @api.depends('dependencia')
    def generar(self):
        print('')


class rh_nomina(models.Model):
    # _inherit = 'hr.employee'
    _inherit = 'mail.thread'
    _name = 'rh_nomina.centroc'
    _rec_name = 'nombre'

    clave = fields.Char('Clave', required=True, track_visibility="always", size=10)
    nombre = fields.Text('Centro de costos', size=200, required=True, track_visibility="always")
    direccion = fields.Many2one('rh_nomina.direccion', string='Direccion de Area', size=200, required=True,
                                track_visibility="always")
    coordinacion = fields.Many2one('rh_nomina.coordinacion', string="Coordinacion", required=True,
                                   track_visibility="always")
    subdependencia = fields.Many2one('rh_nomina.subdependencia', string="Subdependencia", required=True,
                                     track_visibility="always")
    dependencia = fields.Many2one('rh_nomina.dependencia', string="Dependencia", required=True,
                                  track_visibility="always")
    fecha_inicio = fields.Date('fecha inicio', readonly=False, track_visibility="always")
    fecha_final = fields.Date('fecha final', readonly=False, track_visibility="always")
    ad_general = fields.Many2one('rh_nomina.adgeneral', string="Adscripcion General", track_visibility="always")
    ad_particular = fields.Many2one('rh_nomina.adparticular', string="Adscripcion Particular", track_visibility="always")
    unidad = fields.Many2one('rh_nomina.unidad', string="Unidad responsable", track_visibility="always")
    centrot = fields.Many2one('rh_nomina.centrot', string="Centro de trabajo", track_visibility="always")

    _sql_constraints = [('ad_clave_unique', 'unique(clave)', 'Clave repetida')]

    @api.depends('dependencia')
    def generar(self):
        print('')

    class rh_nomina(models.Model):
        # _inherit = 'hr.employee'
        _inherit = 'mail.thread'
        _name = 'rh_nomina.ordenj'
        _rec_name = 'nombre'

        clave = fields.Char('Clave', required=True, track_visibility="always", size=10)
        jerarquia = fields.Text('Jerarquia', size=200, required=True, track_visibility="always")
        fecha_inicio = fields.Date('fecha inicio', readonly=False, track_visibility="always")
        fecha_final = fields.Date('fecha final', readonly=False, track_visibility="always")

        _sql_constraints = [('ad_clave_unique', 'unique(clave)', 'Clave repetida')]

        @api.depends('dependencia')
        def generar(self):
            print('')

    class rh_nomina(models.Model):
        # _inherit = 'hr.employee'
        _inherit = 'mail.thread'
        _name = 'rh_nomina.sindicato'
        _rec_name = 'nombre'

        clave = fields.Char('Clave', required=True, track_visibility="always", size=10)
        nombre = fields.Text('Nombre del sindicato', size=200, required=True, track_visibility="always")
        fecha_inicio = fields.Date('fecha inicio', readonly=False, track_visibility="always")
        fecha_final = fields.Date('fecha final', readonly=False, track_visibility="always")

        _sql_constraints = [('ad_clave_unique', 'unique(clave)', 'Clave repetida')]

        @api.depends('dependencia')
        def generar(self):
            print('')