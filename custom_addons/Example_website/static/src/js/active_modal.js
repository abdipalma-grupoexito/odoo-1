import { Component, xml} from "@odoo/owl"
import { useService  } from "@web/core/utils/hooks"
import { registry } from "@web/core/registry"
import { PopupComponent } from "./modal_dialog"
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog"

export class ActiveModal extends Component{
    static template = xml`<button t-on-click="openPopup"> Saber más</button>`;

    setup(){
        this.dialog = useService("dialog");
    }

    openPopup(){
        this.dialog.add(AlertDialog,{
            title:"Saber más",
            body: "Ventana emergente lanzada para a muestra de la ejecución de javascript.\n",
            close: () => {
                console.log("popup cerrada");
            },
        });
    }
}

/*registry.category("public_components").add("Example_website.active_modal", ActiveModal);*/
registry.category("public_components").add("Example_website.active_modal", ActiveModal);
