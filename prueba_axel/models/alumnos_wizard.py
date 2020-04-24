from odoo import models, fields, api

class alumnosWizard(models.TransientModel):
    _name = 'prueba_axel.wizard'

    def _get_default_alumnos(self):
        return self.env['prueba_axel.alumnos'].browse(self.env.context.get('active_ids'))

    alumnos_ids = fields.Many2many('prueba_axel.alumnos', string='alumnos', default=_get_default_alumnos)
    estado = fields.Boolean(string='Aprobado')

    @api.multi
    def set_alumnos_estado(self):
        for record in self:
            if record.alumnos_ids:
                for alumnos in record.alumnos_ids:
                    alumnos.estado = self.estado