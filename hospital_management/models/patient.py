from odoo import api, fields, models
from datetime import date

class HospitalPetient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Petient"

    name = fields.Char('Patient Name', tracking=True)
    age = fields.Integer('Patient Age', compute='_compute_age', tracking=True, store=True)
    ref = fields.Char('Reference', tracking=True)
    gender = fields.Selection([('male', 'Male'), 
                               ('female', "Female"),
                               ('other', 'Other')], 'Patient Gender', tracking=True)
    dob = fields.Date('Date of Birth')
    active = fields.Boolean('Active', default = True, tracking=True)
    # active fields used to create archive and unarchive option in odoo. must need to add active field in views also.
    # ( here active word is reserved for archive and unarchive option)

    @api.depends("dob")
    def _compute_age(self):
        if self.dob:

        else:

            today = 
            self.age = 0


            self.age = self.dob - date.today().year -
            print(date.today(),"today---------------------------------------")
            print(self.dob,"dob---------------------------------------")
            print((self.dob)-(date.today()),"age---------------------------------------")

            


