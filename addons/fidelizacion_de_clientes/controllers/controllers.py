# -*- coding: utf-8 -*-
# from odoo import http


# class FidelizacionDeClientes(http.Controller):
#     @http.route('/fidelizacion_de_clientes/fidelizacion_de_clientes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fidelizacion_de_clientes/fidelizacion_de_clientes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fidelizacion_de_clientes.listing', {
#             'root': '/fidelizacion_de_clientes/fidelizacion_de_clientes',
#             'objects': http.request.env['fidelizacion_de_clientes.fidelizacion_de_clientes'].search([]),
#         })

#     @http.route('/fidelizacion_de_clientes/fidelizacion_de_clientes/objects/<model("fidelizacion_de_clientes.fidelizacion_de_clientes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fidelizacion_de_clientes.object', {
#             'object': obj
#         })

