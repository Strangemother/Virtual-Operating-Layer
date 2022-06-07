
class Bus {

    emit(name, data) {
        window.dispatchEvent(new CustomEvent(name, { detail:data }))
    }

    on(name, callback) {
        window.addEventListener(name, (e)=>callback(e.detail))
    }

}

class Eventor {
    constructor(selector='.pointer'){
        this.setup.apply(this, arguments)
        this.parent = window
        if(this.autoEnable()) {
            this.enable()
        }
    }

    autoEnable() {
        return false
    }

    setup(selector='.pointer'){
        this.entity = document.querySelector(selector);

    }

    enable(show=true) {
        let parent = this.parent;
        this.bindEntity(parent)
    }

    bindEntity(parent, enable=true){
        let func = ['removeEventListener', 'addEventListener'][+enable]
        let listener = parent[func].bind(parent)

        for(let name of Object.getOwnPropertyNames(this.constructor.prototype)) {

            if(window.hasOwnProperty(`on${name}`)) {
                console.log('Applying', name)
                listener(name, this[name].bind(this))
            }
        }

    }

}

class Watch extends Eventor {

    enable(show=true) {
        let parent = this.entity;
        this.bindEntity(parent)
    }

}

class DelegateMany extends Eventor {

    defaultSelector() { return '.pointer'}

    setup(parent=document, selector=undefined){
        // this.entities = document.querySelectorAll(selector);
        if(selector == undefined) {
            selector = this.defaultSelector()
        }
        console.log('setup')
        this.parent = parent
        this.selector = selector
    }

    inSelection(e) {
        let target = e.target;
        if(!target.parentElement) { return }
        return (new Set(target.parentElement.querySelectorAll(this.selector))).has(target)
    }
}



class WindowHandleDelegate extends DelegateMany {
    /* Watch for any .handle and bubble the event through the bus.*/

    defaultSelector() {
        return '.handle'
    }

    autoEnable() {
        return true
    }

    mouseover(e) { this.busEmit(e) }
    mouseout(e) { this.busEmit(e) }

    busEmit(e){
        if(!this.inSelection(e)) return;
        bus.emit('handle-event', e)
        // console.log(e, e.target)
    }

}

class Iris extends Watch {
    autoEnable() {
        return true
    }

    click(e){
        spawn()
    }
}

let de = new WindowHandleDelegate()
