from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = "patient_id"

    patient_id = fields.Many2one('hospital.patient', string="patient", required=True)
    doctor_id = fields.Many2one('res.users',string="Doctor", required=True)
    medicine_ids = fields.One2many('patient.medicine', 'appointment_id', string="Medicines", required=True)
    active = fields.Boolean('Active', default = True, tracking=True)
    appointment_time = fields.Datetime('Appointment Time', required=True, default=fields.Datetime.now())
    booking_date = fields.Date('Booking Date', default=fields.Datetime.now())
    gender = fields.Selection('Patient Gender', tracking=True, readonly=False, related="patient_id.gender")
    prescription = fields.Html('Prescription')
    priority = fields.Selection([('0','Less'),
                                 ('1','Normal'),
                                 ('2','Intermediate'),
                                 ('3','High'),
                                 ('4','Very High'),
                                 ('5','Extreme')], 'Priority',tracking=True)
    state = fields.Selection([('draft','Draft'),
                              ('in_consultation','In Consultation'),
                              ('done','Done'),
                              ('cancel','Cancel')], 'status', default='draft',tracking=True)

    def action_draft(self):
        self.state = "draft"
    
    def action_in_consultation(self):
        self.state = "in_consultation"

    def action_done(self):
        self.state = "done"

        return { 
            'effect': {'fadeout': 'slow',
                        'message': 'you appointment done Succsessfully',
                        'type': 'rainbow_man',
                      }}
    
    def action_cancel(self):
        self.state = "cancel"