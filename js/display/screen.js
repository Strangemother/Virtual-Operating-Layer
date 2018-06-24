/* A Screen maintains a connection to the Display. A single Screen
will maintain an interface - or any loaded layers and interface
items.

A Screen is a single Root for mounting interfaces.

 */
class DisplayScreen extends Driver {
    /* An extraction of the display unit to render view items. */

    init(){
        /* Tell the system a new screen has attached. */
        system.pubsub.emit('Screen.init', {
            id: this.id()
        })
    }

    mount(sys){
        /* After init readying the Screen instance - the mount()
        function called manually by service or API call attaches any
        relevant extras to the screen - such as waiting views or layer
        booting. */
        lib.log('Mount DisplayScreen')
        sys.pubsub.add('Display.attach', this.displayMount.bind(this))
        sys.pubsub.add('layer.loaded', this.layerLoaded.bind(this))
    }

    displayMount(vdi){
        /* The system has requested this app to render on the given VDI.
        The screen should mount before the Display requests attachment.

        Produce a ready UI.

        s=new DisplayScreen
        s.mount(system)
        // displayMount

        */
        lib.log('Attach Screen.')
        this.createLayers(vdi)

    }

    createLayers(vdi) {
        this.installVDI(vdi)
    }

    installVDI(vdi) {
        let vData = this.data[vdi.name]
        let layers = vData.layers


        system.drivers.loadMountList(layers, function(driverDict){
            let loaded = this.onLoadDrivers(vdi, vData, driverDict)
            this.loadInterface(vdi, vData, loaded);
        }.bind(this))

    }

    onLoadDrivers(vdi, vdiData, driverDict){
        lib.log('onLoadDrivers', vdi.name)
        let layers = {}


        for(let dname in driverDict) {
            lib.log('load', dname)
            layers[dname] = new driverDict[dname]({
                name: vdi.name
                , vdi: vdi
            });

            // A DisplayLayer has a screenLoad func, expecting a xcreen
            layers[dname].screenLoad(this)
        }

        this.loaded = layers;

        for(let n in layers) {
            system.pubsub.emit(`layer.loaded`, {
                id: layers[n].id()
            })
        }

        return layers
    }

    layerLoaded(data) {
        /* A sinle layer has loaded from screenLoad.
        Access the previously loaded layers and start the layer.*/
        system.pubsub.emit('layer.start', data);
        this.loaded[data.id].start()
    }

    loadInterface(vdi, vdiData, loadedLayers){
        /* Cosmetic extension for layers - facilitating a group of
        layers as a bulk driver. */
        let infd = [];

        for (var i = 0; i < vdiData.interface.length; i++) {
            let intfName = vdiData.interface[i]
            let intfClass = new lib[intfName](vdi)
            intfClass.mount(this, loadedLayers)
        }
    }
}


lib.mount({DisplayScreen})
