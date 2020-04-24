# -*- coding: utf-8 -*-

from odoo import models, fields, api

class res_partner(models.Model):
    _inherit='res.partner'

    passed_override_write_function = fields.Boolean(string='Has passed our super method')


    @api.model
    def create(self,values):
        record= super(res_partner,self).create(values)
        record['passed_override_write_function'] = True
        return record
