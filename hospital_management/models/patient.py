from odoo import api, fields, models
from datetime import date

class HospitalPetient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Petient"

    name = fields.Char('Patient Name', tracking=True, required=True)
    age = fields.Integer('Patient Age', compute='_compute_age', tracking=True)
    ref = fields.Char('Reference', tracking=True, required=True)
    gender = fields.Selection([('male', 'Male'), 
                               ('female', "Female"),
                               ('other', 'Other')], 'Patient Gender',required=True, tracking=True)
    dob = fields.Date('Date of Birth', required=True)
    active = fields.Boolean('Active', default = True, tracking=True)
    appointment_ids = fields.One2many('hospital.appointment','patient_id', string="Appointments")
    # active fields used to create archive and unarchive option in odoo. must need to add active field in views also.
    # ( here active word is reserved for archive and unarchive option)

    # @api.depends("dob")
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.dob:
                rec.age = today.year - rec.dob.year
            else:
                rec.age = 0
