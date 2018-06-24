class ViewInterface extends ExposedDriver {

    static wakeIdentity(){
        /* The base interface will automatically mount
        given the event name. _hook_ will instiate the driver
        correctly. */
        return `Interface.defaultStart`
    }

    static wake(name){
        /* Preliminary start method. Used to inboke pre conditions before hook.*/
    }

    hook(name, data){
        /* capture the GUI the data is the wake event information.
        Stated by the wake name. */
        console.log('ViewInterface hook', name)
        this.data = data
        this.displayRenderer = new DisplayRenderer()
        this.cleanStart()
    }

    cleanStart(){
        let _el = lib._logger.el
        window.ii = this

        let rootName = 'root';
        let rootLayers = [];

        let next = []
        // Hook root:
        for (var i = 0; i < this.data.interface.layers.length; i++) {
            let lSet = this.data.interface.layers[i];
            let name = lSet.layer.data.name;
            if(name == rootName) {
                this.hookRoot(lSet.layer, lSet.config)
                rootLayers.push([lSet.layer, lSet.config])
            } else {
                next.push([lSet.layer, lSet.config])
            }
        }

        for (var i = 0; i < next.length; i++) {
            let layer, config = next[i];
            this.hookLayer(rootLayers, layer, config)
        }
    }

    hookRoot(layer, config){
        console.log('Hook root layer')
        this.rv = 0
        this._size = layer.data.vdi.dimensions.viewport
        this.drawFPS = this.data.definition.layer.space.drawFPS
        layer.space.context.animFrame.setRenderfunction(this.step.bind(this))

        this.hookEvents(layer)
        this.runRoutine()
        let t = this.hookLogger()
        this.sendInitEvent(t)
    }

    sendInitEvent(text) {
        // Send initial value, prime for incomind encoded.

        let d = {
            // The type of message sent
            type: 'data'
            , interface: this.data.interface.data
        }

        this.thread.send(d)
        return this.sendToThread(text)
    }

    runRoutine(){
        /* perform the interactive render and step sequence through
        the threading.*/
        this.encoding = document.characterSet.toLowerCase()
        this.encoder = new TextEncoder(this.encoding)
        this.decoder = new TextDecoder(this.encoding)
        console.log('.. Starting thread')
        this.thread = lib.threadPool.startThread('/js/display/dedicatedThread.js', 'displayThread')
        system.pubsub.add('thread.event', this.threadEvent.bind(this))
    }

    threadEvent(data) {
        /* Eww... */
        try {

            let v = this.decoder.decode(data.data.data);
            console.log('interface.threadEvent', v)
        } catch(e){
            // console.log('threadEvent d', data.data.data)
            this.displayRenderer.actionEvent(data.data)
        }
    }

    sendToThread(data) {
        var uint8_array = this.encoder.encode(data)
        var array_buffer = uint8_array.buffer;
        // now transfer array buffer
        console.log('send', array_buffer)
        this.thread.send(array_buffer, [array_buffer])
    }

    hookLogger(){
        this.logParent = lib._logger.el.parentNode
        lib._logger.el.remove()
        return lib._logger.el.textContent
    }

    hookEvents(layer){
        let c = layer.space.getCanvas();

        let createEvent = function(n){
            c.addEventListener(n, function(e) {
                this[`${n}Event`](layer, e);
            }.bind(this))
        }.bind(this)

        createEvent('mousedown')
        createEvent('mouseup')
    }

    mousedownEvent(layer, event) {
        console.log('mousedown')
    }

    mouseupEvent(layer, event) {
        console.log('mouseup')
    }

    step(ctx) {
        // this.data.interface.data.dimensions.viewport
        let vp = this._size
        let h = this._size.height;
        this.clear(ctx)

        ctx.strokeRect(2,2, this._size.width - 8, h - 8)

        this.drawFPS(ctx, 20)
        this.displayRenderer.step(ctx)

        if(this.rv > h) {
            this.rv = 0
        }

        this.rv += 1

        // Draw box representing clearing

        //ctx.clearRect(0,0, this._size.width, this._size.height)
        //ctx.restore()
        this.marchingClock(ctx)
        //ctx.restore()
    }

    clear(ctx){
        let vp = this._size
        let h = this._size.height;
        // Clear
        ctx.save()
        ctx.setTransform(1, 0, 0, 1, 0, 0);
        ctx.clearRect(0, 0, vp.width, h)
        ctx.restore()
        ctx.beginPath()
    }

    marchingClock(ctx){
        //ctx.closePath()
        ctx.beginPath()
        // ctx.save()
        ctx.fillStyle = `rgb(0, ${this.rv % 255}, 0)`
        //ctx.save()
        ctx.lineWidth = 3
        ctx.rect(55, this.rv + 5, 20,20)
        ctx.strokeStyle = 'rgb(0,255,0)'
        ctx.strokeRect(50, this.rv, 30,30)
        ctx.lineWidth = 1
        ctx.fill()
    }

    hookLayer(roots, layer, config) {
        console.log('Hook secondary layer')
    }
}

class DisplayRenderer {
    /* Given an object input, convert the object into a renderable entity.
    store that entity into a step list.
    update the entity when instucted.

    It's essentially a mini-api for the thread, allowing turtle walking
    with objects through the pipe.*/
    constructor(){
        this.displayList = {}
        this._aCount = 0
        window.dl = this;
    }

    actionEvent(e){
        /* given a thread message, action the routine */

        let data = e.data;
        if(it(data).is('string')) {
            this.logString(data)
            return
        }

        for(let k in data) {
            // a_display
            if(this[`a_${k}`] == undefined) {
                console.warn('Unknown thread event key:', k)
                continue
            }

            let dv = data[k];
            if(dv == undefined) {
                console.warn('Undefined data for actionEvent', k)
            }
            this[`a_${k}`](dv, e)
            this._aCount += 1
        }
    }

    logString(data){
        console.log(data)
    }

    a_display(data, message) {
        /* given a display routine, add the element to the display list.*/
        this.displayList[data.id] = {layers: data.layers}
    }

    a_change(data, message) {

        // Accept the new layer and replace the indexed value of the
        // existing layers.
        let layer = this.displayList[data.id].layers[data.index]
        this.displayList[data.id].layers[data.index] = data.layer
        // = {layers: data.layers}
    }

    a_destroy(data, message) {
        /* destroy the entity with the given id.*/
        delete this.displayList[data.id]
    }

    step(ctx){
        /* Iterate internal*/
        let dl = this.displayList
        for(let id in dl) {
            //ctx.save()

            //for (var i = 0; i < dl.length; i++) {
            for (var j = 0; j < dl[id].layers.length; j++) {
                let layer = dl[id].layers[j];
                let val = layer.value;
                if(val) {
                    [   // no args call...
                        () => {}
                        // one argument - just a method
                        , (f) => ctx[f]()
                        // a method with arguments.
                        , (f) => ctx[f].apply(ctx, val[1])

                    ][val.length](val[0])
                }

                if(layer.attr) {
                    ctx[layer.attr[0]] = layer.attr[1]
                }
            }
            //ctx.restore()
        }
    }
}

lib.driverMount(ViewInterface)
