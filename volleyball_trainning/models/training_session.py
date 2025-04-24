from odoo import models, fields, api
from datetime import datetime

class VolleyballSession(models.Model):
    _name = 'volleyball.session'
    _description = 'Volleyball Training Session'

    name = fields.Char(string='Session Name', required=True)
    date = fields.Datetime(string='Date', default=fields.Datetime.now)
    duration = fields.Float(string='Duration (hours)')
    focus_area = fields.Selection([
        ('serving', 'Serving'),
        ('passing', 'Passing'),
        ('setting', 'Setting'),
        ('attacking', 'Attacking'),
        ('blocking', 'Blocking'),
        ('defense', 'Defense'),
    ], string='Focus Area')
    coach_notes = fields.Text(string='Coach Notes')
    player_ids = fields.Many2many('volleyball.player', string='Players')