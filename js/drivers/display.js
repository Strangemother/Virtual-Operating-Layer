/* Raw display driver, maintaining many screens.

A more complex driver the 'display' defines drawable point.

In this archtexture the display driver adapts physical screens
with a gui hook through the pubsub - or a binary thread.

The main thread (this) - maintains the IO of display, brokering rendering
threads

The driver display should be driven by API and pubsub - as browser screens
will not match VOL screens.
 */

class Display extends Driver {
    /* display class handles the metal connection to the API and spawn
    DisplayScreens.

    Once mounted to a system, download FILES.display.
    Install a
    */
    init(){
        lib.log('Display Driver init')
        this.loadDetect()
    }

    loadDetect(){
        /* load the init data or detect new, given the init memory information.*/
        let ds = this.detectScreens()
        if(this.data.auto == true) {
            this.vdi = ds
        } else {
            this.displays = system.memory.get('Display.init')
            if(this.displays == undefined) {
                this.vdi = ds;
                system.memory.put('Display.init', ds)
            }
        }
    }

    detectScreens(){
        /* return a set of displays, subscribed.*/

        return {
            attached: [
                {
                    id: 'root'
                    , size: {
                        width: screen.availWidth
                        , height: screen.availHeight
                    }
                    , viewport: {
                        width: window.innerWidth
                        , height: window.innerHeight
                    }
                }
            ]
            , count: 1
        }
    }

    mount(sys){
        Assets.load(FILES.display, this.onDisplayDrivers.bind(this))

        // Attach a listener.
        sys.pubsub.add('Display.add', this.mountScreens.bind(this))
        sys.pubsub.add('Screen.init', this.screenInit.bind(this))

        this.mountScreens(this.vdi)
    }

    screenInit(){
        /* A screen entity has announced it's existence. */
        lib.log('Display heard init')
        setTimeout(function(){
            this.announceAttach(this.getVDI('root'), 'root')
        }.bind(this), 100)
    }

    getVDI(name) {
        for (var i = 0; i < this.vdi.attached.length; i++) {
            if(this.vdi.attached[i].id == name) {
                return this.vdi.attached[i]
            }

        }
    }

    mountScreens(displays){
        for (var i = 0; i < displays.attached.length; i++) {
            let vp = displays.attached[i].viewport;
            let dn = displays.attached[i].id;
            this.attachViewport(vp, dn)
        }
    }

    attachViewport(dimensions, name) {
        this.announceAttach(dimensions, name)
    }

    announceAttach(dimensions, name){
        lib.log('Announcing display to waiting screen')
        system.pubsub.emit('Display.attach', { name, dimensions })
    }

    onDisplayDrivers(){
        /* Display drivers are loaded. The async mounting may have finished.
        Rendering can begin.*/
        system.pubsub.emit('Display.mount', this.vdi)
        system.drivers.installDriver(DisplayScreen)
    }
}


class DisplayLayer {

    constructor(data) {
        this.data = data || {}
        this.init()
    }

    static id(){
        /* return a unique ID for this driver, used for
        memory mapping*/
        return `layer.${this.name}`
    }

    id(){
        return this.constructor.id()
    }

    init(){
        /* The drvier is initialized. All the required settings are ready
        for use. The driver is not mounted.*/
        lib.log(`init ${this.id()}`)
    }

    mount(screen, layers){
    }
}

lib.driverMount(Display)
