# -*- coding: utf-8 -*-

from odoo import models, fields, api


class res_partner(models.Model):
    _inherit = ['res.partner']
    passed_override_write_function = fields.Boolean(string='Has passed our super method')

    @api.model
    def create(self, values):
        # Sobrescribir con el metodo super
        record = super(res_partner, self).create(values)

        # Change the values of a variable in this super function
        record['passed_override_write_function'] = True
        print 'Passed this function. passed_override_write_function value: ' + str(
            record['passed_override_write_function'])

        # Return the record so that the changes are applied and everything is stored.
        return record
    @api.multi
    def write(self, values):
        values['street'] = "Vacio"
        # Override the original create function for the res.partner model
        wr = super(res_partner, self).write(values)
        # Change the values of a variable in this super function
        #print 'Passed this function. passed_override_write_function value: ' + str(
        #    wr['street'])
        # Return the record so that the changes are applied and everything is stored.
        return wr

    @api.multi
    def unlink(self):
        # Override the original create function for the res.partner model
        wr = super(res_partner, self).unlink
        # Change the values of a variable in this super function
        # print 'Passed this function. passed_override_write_function value: ' + str(
        #    wr['street'])
        # Return the record so that the changes are applied and everything is stored.
        print "si jala el borrar c8"
        return wr
