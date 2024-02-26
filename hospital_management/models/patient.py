from odoo import api, fields, models

class HospitalPetient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Petient"

    name = fields.Char('Patient Name')
    age = fields.Integer('Patient Age')
    ref = fields.Char('Reference')
    gender = fields.Selection([('male', 'Male'), 
                               ('female', "Female"),
                               ('other', 'Other')], 'Patient Gender')
    active = fields.Boolean('Active', default = True)
    # active fields used to create archive and unarchive option in odoo. must need to add active field in views also.
    # ( here active word is reserved for archive and unarchive option)
