/* An interface is a stack of graphical layers - managed by a Screen.*/

class InterfaceLayer extends DisplayLayer {
    /* An extraction of the display unit to render view items. */

    static id(){
        /* return a unique ID for this driver, used for
        memory mapping*/
        return `Interface`
    }

    init(){
        /* Tell the system a new screen has attached. */
        this.layers = [];

        system.pubsub.emit(`${this.id()}.init`, {
            id: this.id()
        })
    }

    mount(screen, layers){
        //console.log('Mount interface')
        // Test existing layers - download any extra drivers.
        // edit UI - mounting real gui.

        /* For this interface to proceed, it requires
        a canvas layer. this is collected from the given layers
        or installed.*/
        let rootRequiredLayer = 'layer.Canvas'
        let root = layers[rootRequiredLayer]

        this.mountLayer(root, screen.data)
    }

    mountLayer(layer, config) {
        /* Given a rendering layer, mount into the interface and begin
        processing.
        the config object is merged on top of INIT_SYSTEM_MEMORY - */

        // Get unique name for layer and config.
        let configureName = `${this.id()}.${layer.data.name}`
        let layerConfig = Object.assign({}, system.memory.get(configureName), config[configureName])
        this.data.layerConfig = layerConfig
        Assets.load(FILES.interface, function(){
            this.onLoadLayerImplements(layer, layerConfig)
        }.bind(this))
    }

    onLoadLayerImplements(layer, config){
        /* Layers for this interface are loaded, Install and boot.*/
        //console.log('Mounted layer', layer.id())
        let len = this.layers.push({ layer, config })
        this.setRootIndex(len-1)
        this.startLayer(len-1)
    }

    setRootIndex(index) {
        /* Set the index of the root item.*/
        this._rootIndex = index
    }

    startLayer(index){
        /* Given an index from the internal layers, begin integration and processing
        */
        let layerSet = this.layers[index]
        let dataName = `${layerSet.layer.data.name}-${index}`
        if(this.data[dataName] == undefined) {
            this.data[dataName] = {}
        }

        this.start({ layer: layerSet.layer, config: layerSet.config, index, data: this.data[dataName]})
    }

    start(layerDefinition){
        // Mount expected canvas layer, start draw routines.
        //console.log('Start layer', layerDefinition.index)

        // Will appear in the ExposedDriver(NAME).hook()
        system.pubsub.emit(`${this.id()}.${layerDefinition.config.start}`,{
            definition: layerDefinition
            , interface: this
        })
    }
}

lib.mount({[InterfaceLayer.id()]:InterfaceLayer})

