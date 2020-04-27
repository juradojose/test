from odoo import models, fields, api

class materiaWizard(models.TransientModel):
    _name = 'prueba_axel.wizardmat'

    def _get_default_materia(self):
        return self.env['prueba_axel.materias'].browse(self.env.context.get('active_ids'))

    materias_ids = fields.Many2many('prueba_axel.materias', string='Materias', default=_get_default_materia)
    creditos = fields.Integer(string='Creditos')

    @api.multi
    def set_alumnos_estado(self):
        for record in self:
            if record.materia_ids:
                for materias in record.alumnos_ids:
                    materias.estado = self.creditos