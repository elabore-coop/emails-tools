from odoo import models, fields, api


class Message(models.Model):

    _inherit = "mail.message"

    @api.model
    def _get_default_from(self):
        if not self.mail_server_id:
            mail_server = self.env["ir.mail_server"].search(
                [], limit=1, order="sequence"
            )
        else:
            mail_server = self.mail_server_id
        if mail_server.force_from:
            return mail_server.form_forced_address
        else:
            return super(Message, self)._get_default_from()

    @api.model
    def _get_default_reply_to(self):
        if not self.mail_server_id:
            mail_server = self.env["ir.mail_server"].search(
                [], limit=1, order="sequence"
            )
        else:
            mail_server = self.mail_server_id
        if mail_server.force_reply_to:
            return mail_server.reply_to_forced_address

    reply_to = fields.Char(default=_get_default_reply_to)
