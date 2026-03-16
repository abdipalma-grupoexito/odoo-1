from odoo import fields, models

class Redirect(models.Model):
    _name = 'example.website.redirect'

    name = fields.Char()


    def action_open_another_view(self):
        return{
            'name':"cart_view",
            'tyep': "ir.actions.act_window",
            'res_model' : 'target.model.name',
            'view_mode' : 'list,form',
            'view_type': 'form',
            'target' : 'current',
            'res_id' : self.related_record_id.id,
            'view_id' : self.env.ref('Example_website.cart_').id,

    }