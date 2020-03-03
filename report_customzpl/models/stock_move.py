# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class StockMove(models.Model):
    _inherit = 'stock.move.line'
    w_num_imp = fields.Integer('Impresiones', required=False)
