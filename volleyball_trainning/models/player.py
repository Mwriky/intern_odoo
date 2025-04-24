from odoo import models, fields, api

class VolleyballPlayer(models.Model):
    _name = 'volleyball.player'
    _description = 'Volleyball Player'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    position = fields.Selection([
        ('setter', 'Setter'),
        ('libero', 'Libero'),
        ('middle', 'Middle Blocker'),
        ('outside', 'Outside Hitter'),
        ('opposite', 'Opposite Hitter'),
    ], string='Position')
    skill_level = fields.Selection([
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ], string='Skill Level')
    active = fields.Boolean(string='Active', default=True)
    session_ids = fields.Many2many('volleyball.session', string='Training Sessions')