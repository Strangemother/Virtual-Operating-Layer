/* Map all keys through a central dispatch*/

class Keyboard extends Driver {
    /*
        Keyboard base driver simply captures the input
        self keyup etc... and emits through the pubsub.
     */
    static id(){
        return `base.${this.name}`
    }

    init() {
        lib.log('Driver Keyboard')

    }

    emit(event) {
        system.pubsub.emit(`${this.id()}.${event.type}.`, event)
    }

    addListener(name) {
        self.addEventListener(name, this[name].bind(this), true)
    }

    events(){
        return ['keydown', 'keyup', 'keypress']
    }

    mount() {
        super.mount()
        for(let name of this.events()){
            this.addListener(name)
        }
    }

    keydown(event){
        this.emit(event)
    }

    keyup(event){
        this.emit(event)
    }

    keypress(event){
        this.emit(event)
        lib.log(event.type, event.key)
    }

}

lib.driverMount(Keyboard)
