from odoo import models, fields

class crud(models.Model):
    _name = 'crud'
    _description = 'karepelah'

    name = fields.Char(string='Nama', required=True)
    entah = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4')
    ], string='Entah', default='1', required=True)