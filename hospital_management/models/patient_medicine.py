from odoo import api, fields, models
from datetime import date

class PetientMedicine(models.Model):
    _name = "patient.medicine"
    _description = "Petient Medicine"

    appointment_id = fields.Many2one('hospital.appointment', string="Appointment Patient")
    product_id = fields.Many2one('product.product', string="Medicine", required=True)
    price = fields.Float(related='product_id.list_price', string="Unit Price")
    qty = fields.Integer("Qty", default=1)