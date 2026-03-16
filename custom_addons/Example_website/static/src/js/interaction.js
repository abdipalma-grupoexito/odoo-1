import {Interaction} from "@web/public/interaction"
import {registry} from "@web/core/registry"


export class BasicInteraction extends Interaction{
    static selector=".myModal"
    setup(){
        this.state = {
            count:0
        };
    }

    dynamicContent={
        ".btn":{
            "t-on-click": () => this.popup(),
        }
    }

    popup(){
        const myModal = new bootstrap.Modal(document.getElementById('myModal'));
        myModal.show();
    }
}

registry.category("public.interactions").add("Example_website.basic_interaction", BasicInteraction);