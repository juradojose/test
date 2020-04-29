from odoo import api , models, fields
from odoo.exceptions import ValidationError
class RepasoCapaitacion(models.Model):
    _name="repaso.main"
    _rec_name="nombre_dueno"

    its_traveling=fields.Boolean('its_traveling',invisible=1,readonly=True, store=True)

    tickets=fields.Selection(selection=[
        ('theater','Cine'),
        ('conc','Concierto'),
        ('flygth','Vuelo'),
        ('train','Tren'),
        ('bus','Autobus')
    ],string="Tipo de ticket",required=True)
    nombre_dueno=fields.Many2one('res.partner',string="Nombre Cliente")
    fecha_ticket=fields.Date(string="Hola", default= lambda self: fields.datetime.now())
    costo=fields.Float('Costo de boleto', digits=(6,2),computed="calculate_cost", readonly=False, store=True)
    destino=fields.Selection(selection=[
        ('national','Nacional'),
        ('internacional','Internacional')
    ], string="Tipo de Destino",store=True)
    lugar_destino=fields.Char(string="Lugar Destino",store=True)
    descuento=fields.Float(string="Descuentos % :", digits=(3,2))

    @api.onchange('tickets')
    def hideMethod(self):
        if(self.tickets == 'train' or self.tickets=='flygth' or self.tickets=='bus' ):
            self.its_traveling=True
        else:
            self.its_traveling=False

        if(self.its_traveling):
            if(self.tickets=='flygth'):
                self.costo=6300.00
            if(self.tickets=='train'):
                self.costo=520.00
            if(self.tickets=='bus'):
                self.costo=500.00
        else:
            if(self.tickets=='theater'):
                self.costo=50.00
            if(self.tickets=='conc'):
                self.costo=500.00

    @api.onchange('descuento')
    def discount(self):
        message=""
        if(self.descuento > 0 and self.descuento <=50):
            descuento = self.costo*(self.descuento/100)
            self.costo=self.costo - descuento
        else:
            if(self.descuento > 50):
                message='mayor al 50%'
            elif(self.descuento <0):
                message="negativo"
            raise ValidationError('El descuento no debe ser '+message)