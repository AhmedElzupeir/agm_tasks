# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class WarehouseRestrict(models.Model):
	_inherit = 'res.users'

	warehose_ids = fields.Many2many('stock.warehouse', string='Warehouses' )
