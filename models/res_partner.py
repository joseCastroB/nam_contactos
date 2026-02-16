from odoo import models, fields 

class ResPartner(models.Model):
    _inherit = 'res.partner'

    nam_contacto = fields.Char(string='Contacto')

    nam_entidad_bancaria = fields.Char(string='Entidad Bancaria')

    nam_cta_cte = fields.Char(string='CTA. CTE. (S/.)')
    nam_cci = fields.Char(string='CCI (S/.)')
    nam_cta_cte_usd = fields.Char(string='CTA. CTE. (USD)')
    nam_cci_usd = fields.Char(string='CCI (USD)')
    nam_cta_detracciones = fields.Char(string='Cta. Detracciones')