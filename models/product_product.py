# -*- coding: utf-8 -*-
from odoo import models, api, fields
from odoo.exceptions import AccessError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    editable_by_group = fields.Boolean('Editable por grupo', default=False)

    @api.multi
    def write(self, vals):
        current_user = self.env.user
        if not current_user.has_group('jr_editable_sale.group_custom1'):  # Reemplaza 'nombre_del_grupo' por el nombre real de tu grupo
            if any(order.state in ('sale', 'done', 'cancel') for order in self):
                raise AccessError("No tienes permisos para modificar líneas de pedido confirmadas, realizadas o canceladas.")
        return super(SaleOrder, self).write(vals)