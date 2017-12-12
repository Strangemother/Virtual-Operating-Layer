class InterfaceLayer extends DisplayLayer {
    /* An extraction of the display unit to render view items. */

    static id(){
        /* return a unique ID for this driver, used for
        memory mapping*/
        return `Interface`
    }

    init(){
        /* Tell the system a new screen has attached. */
        system.pubsub.emit(`${this.id()}.init`, {
            id: this.id()
        })
    }

    mount(screen, layers){
        console.log('Mount interface')
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

        debugger;
    }

    loadImplement(cls, layer, config) {
        /* Load the given class into the given layer using any options from the
        config object. */
        console.log('load', cls.name, 'into', layer.id())
    }

    getSize(){
        return this.data.vdi.dimensions.viewport
    }

    start(drawFunc){
        lib.log('start canvas')
        let el = this.space.config.canvas;
        this.present(el)
        this.space.draw(drawFunc || drawFunction)
    }

    present(el){
        let borderWidth = 2
        let color = 'red'
        document.body.append(el)

        let size = this.getSize()
        el.width = size.width - (borderWidth * 2)
        el.height = size.height - (borderWidth * 2)

        let cssEl = document.createElement('style');
        cssEl.id = `${this.id()}.style`
        cssEl.innerHTML = `canvas { border: solid ${borderWidth}px ${color}; top: 0px; left: 0px; position: absolute; }
        body { margin: 0; overflow: hidden}`
        document.body.append(cssEl)
        window.scrollTo(0, 0)
    }
}

lib.mount({[InterfaceLayer.id()]:InterfaceLayer})

