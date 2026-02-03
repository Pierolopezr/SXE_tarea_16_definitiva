# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class fidelizacion_de_clientes(models.Model):
#     _name = 'fidelizacion_de_clientes.fidelizacion_de_clientes'
#     _description = 'fidelizacion_de_clientes.fidelizacion_de_clientes'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

