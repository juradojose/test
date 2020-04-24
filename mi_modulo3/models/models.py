# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

#comentarios


class mi_wizard(models.TransientModel):
    _name = 'modulo3.wizard'
    _description = 'wizard1'

    def _default_bands(self):
        return self.env['mi_modulo3.mi_modulo3'].browse(self._context.get('active_ids'))
    
    #session_ids = fields.Many2many('modulo3.session',String="Sessions",required=True,default=_default_sessions)

    bandas_ids = fields.Many2many('mi_modulo3.mi_modulo3', String="BANDAS", default=_default_bands)

    
    def suscribe(self):
        for record in self:
            if record.bandas_ids:
                for banda in record.bandas_ids:
                    banda.pais_origen = self.pais_origen
            

class discos(models.Model):
    _name = 'discos.modulo3'
    _rec_name = 'name'
    _description = 'discos'
    name = fields.Char(string="Nombre",required=True)
    #album = fields.One2many('mi_modulo3.mi_modulo3','discos')
    album =fields.Many2one('mi_modulo3.mi_modulo3')



class mi_modulo3(models.Model):
    _name = 'mi_modulo3.mi_modulo3'
    _description = 'mi_modulo3.mi_modulo3'

    banda = fields.Char(string="BANDA O GRUPO",required=True)
    imagen = fields.Binary()
    genero = fields.Char(string="GENERO", size=12)
    pais_origen = fields.Char(string='PAIS DE ORIGEN')
    estatus = fields.Selection([('on','Activa'),('off','Retirados')],default='on') 
    enlace = fields.Char(string="WEBSITE")
    valoracion = fields.Selection([('1','Malo'),('2','Regular'),('3','Bueno'),('4','Excelente')])
    """total_de_discos = fields.Integer(
        compute='get_total_discos',
        string='Total de discos',
        readonly=True,
    )"""
    #discos = fields.Many2one("discos.modulo3")
    discos = fields.One2many("discos.modulo3","album")

    state = fields.Selection([
        ('inicio', 'Inicio'),
        ('casi', 'Casi'),
        ('hecho', 'Hecho'),
        ],default='inicio')
    


    def get_total_discos(self):
        self.total_de_discos = 529


    """def act_btn(self):
        self.write({'banda':'No especificada','genero':'Desconocido','pais_origen':'Desconocido'})

     
    def act_btn2(self):
        self.write({'banda':' ','genero':' ','pais_origen':' '})"""


    @api.constrains('banda','genero')
    def verificar_nombre(self):
        if not self.banda or not self.genero:
            raise exceptions.ValidationError("NO DEBE HABER CAMPOS VACIOS")

     

    
   
    
    def casi_progressbar(self):
        self.state="casi"
 
    #This function is triggered when the user clicks on the button 'In progress'
    
    def hecho_progressbar(self):
        self.state='hecho'

    
