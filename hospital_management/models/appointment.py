from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"

    patient_id = fields.Many2one('hospital.patient', string="patient", required=True)
    active = fields.Boolean('Active', default = True, tracking=True)
    appointment_time = fields.Datetime('Appointment Time', required=True, default=fields.Datetime.now())
    booking_date = fields.Date('Booking Date', default=fields.Datetime.now())
    gender = fields.Selection('Patient Gender', tracking=True, readonly=False, related="patient_id.gender")