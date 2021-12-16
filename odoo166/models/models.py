# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class odoo166(models.Model):
#     _name = 'odoo166.odoo166'
#     _description = 'odoo166.odoo166'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api

class persona(models.Model):
	_name = 'odoo166.juegos'
	_description = 'modelo juegos'

	name = fields.Char(string='Nombre', required=True)
	imagen = fields.Char(string='Imagen', required=True)
	precio = fields.Char(string='Precio', required=True)
	date = fields.Date(string="Fecha Salido", default=fields.Date.context_today)