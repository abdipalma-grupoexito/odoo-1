/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component, useState} from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class MyModal extends Component{
    static template = "Example_website.my_modal_template";

    setup(){
        this.state = useState({
            value: ""
        });

        this.orm=useService("orm");
        this.notification = useService("notification");
    }

    confirm(){
        this.notification.add("Action confirmed", { type: "success"});
        this.props.close();
    }
}

registry.category("actions").add("Example_website.modal_dialog", MyModal);