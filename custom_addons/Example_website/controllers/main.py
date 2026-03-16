from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class Main(http.Controller):
    @http.route('/Example', type='http', auth='public', website=True)
    def custom_page(self, **kw):
        user_name = request.env.user.name
        return request.render('Example_website.Example_website_template',{
            'user_name': user_name,
        })

class WebsiteSaleInherit(WebsiteSale):
    @http.route([
            '/Example/shop',
            f'/Example/shop/page/<int:page>',
            f'/Example/shop/category/<model("product.public.category"):category>',
            f'/Example/shop/category/<model("product.public.category"):category>/page/<int:page>',
        ], type='http', auth='public', website=True)
    # def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, tags='', **post):
    #     res = super(WebsiteSaleInherit, self).shop(page=0, category=None, search='', min_price=0.0, max_price=0.0, tags='', **post)
    #     print("Inherited odoo shop.....", res)
    #     return res
    def custom_page(self, **kw):
        user_name = request.env.user.name
        return request.render('Example_website.custom_cart_lines',{
            'user_name': user_name,
        })
