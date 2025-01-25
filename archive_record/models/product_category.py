from odoo import fields, models


class ProductCategory(models.Model):
    _inherit = "product.category"

    active = fields.Boolean('Active', default=True)