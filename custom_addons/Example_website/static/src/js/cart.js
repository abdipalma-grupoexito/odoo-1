import { Component, xml} from "@odoo/owl"
import { useService  } from "@web/core/utils/hooks"
import { registry } from "@web/core/registry"

export class Cart extends Component{
    static template= "cart_shop_template";

    setup(){

    }


}

registry.category("public_components").add("Example_website.cart", Cart);