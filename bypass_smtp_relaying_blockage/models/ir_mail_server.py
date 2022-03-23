from odoo import api, fields, models, tools, _


class IrMailServer(models.Model):

    _inherit = "ir.mail_server"

    force_from = fields.Boolean(string=_("Force From address"))
    from_forced_address = fields.Char(string=_("Forced From address"))
    force_reply_to = fields.Boolean(string=_("Force Reply To address"))
    reply_to_forced_address = fields.Char(string=_("Forced Reply To address"))
