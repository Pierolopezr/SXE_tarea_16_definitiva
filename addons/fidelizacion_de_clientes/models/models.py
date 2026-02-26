# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fidelizacion_de_clientes(models.Model):
    _inherit = 'res.partner'
    Nivel_de_fidelidad = fields.Char(string="Nivel de didelidad",readonly=True,compute="_calcular_fidelizacion", store=True)
    Codigo_de_socio = fields.Char("Codigo de socio")

    @api.depends('Codigo_de_socio')
    def _calcular_fidelizacion(self):
        for record in self:
            cods = record.Codigo_de_socio

            if cods:
                if cods[0] == 'G':
                    record.Nivel_de_fidelidad = "Gold"
                else:
                    record.Nivel_de_fidelidad = "Premium"
            else:
                record.Nivel_de_fidelidad = "Estándar"

