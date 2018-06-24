/* Provide the ability to render text.
Literally characters - not much else.*/

class Position {

    constructor(x,y) {
        this._v = [x, y]
    }

    get x(){
        return this._v[0]
    }

    get y(){
        return this._v[1]
    }
}

class CanvasNode extends DisplayLayer {
    /* Everything inherits the basic canvas node. */

    defaultConfig(){
        return {
            id: Math.random().toString(32).slice(2)
            // stroke, clear
            , type: 'rect'
        }
    }

    init(){
        debugger
        this.data = Object.assign(this.defaultConfig(), this.data)
        this._type = this.constructor.name;
    }

    display(pipe) {
        /* Display the canvas node by sending a new setof layers through
        the pipe to the waiting canvas,
        This mat be called more than once. Each call will recompile the
        layers and send an attachment.

        Sending consecutive display messages may orphan previous layers.
        Call 'destroy' or remount to force a complete recycle of the node.*/
        if(this.pipe != undefined) {
            if( pipe != undefined) {
                if( pipe != this.pipe) {
                    /* a replacement.*/
                    console.log('PIPE Changed.')
                }
            } else {
                /* Default pipe given.*/
                pipe = this.pipe
            }
        }

        this.compute()
        this.pipe = pipe;
        let c = this.instructions()
        this.compiled = c;
        this.attachments = {}
        this.attachLayers(c.layers)

        pipe.send({ display: {id: c.id, layers: this.getValue(c.layers)}}, false)
    }

    remove(pipe) {
        /* Send a destroy message to the canvas - deleting the layers allocated
        to this node.*/
        if(pipe == undefined) {
            pipe = this.pipe
        }

        pipe.send({
            destroy: {id: this.data.id }
        }, false);

    }

    remount(pipe) {
        /* Call remove - to destory the existing node from the canvas, then
        display(), to recreate the node.*/
        if(pipe == undefined) {
            pipe = this.pipe
        }

        this.remove(pipe)
        this.display(pipe)
    }

    attachLayers(layers){
        /* Iterate the fgiven layers, binding to 'attachements' using the
        'attach' keyword for every layer object.
        When a property is set on the node - if a layer is attached by
        property name - the entire layer is recomuted and sent
        to the render as a layer replacement.*/
        for (var i = 0; i < layers.length; i++) {
            let layer = layers[i]

            if(Instruction.isPrototypeOf(layer)) {
                console.log('Found complex Layer')
                let InstuctionClass = layer;
                let iLayer = new InstuctionClass();
                // Call the sub list, resolving first
                // phase.
                layer = iLayer

            }

            if(layer.attach) {
                let aset = layer.attach

                if(IT.g(layer.attach).is('function')) {
                    aset = layer.attach()
                }

                if(aset == undefined) continue;

                for (var k = 0; k < aset.length; k++) {
                    let key = aset[k];

                    if(this.attachments[key] == undefined) {
                        this.attachments[key] = []
                    };
                    this.attachments[key].push(i)
                }
            }


        }
    }

    getValue(layers, data){
        /* Given an array of layers, return an array of transferable layers.
        Conveting all functional call and packing the layers ready for transport.
        */
        let r = []

        if(layers == undefined) {
            layers = this.compiled.layers;
        }

        if(data == undefined) {
            data = this.data
        }

        r = this.convertLayers(layers, data, r)
        return r
    }

    compute(data) {
        if(data==undefined) {
            data = Object.assign({}, this.config)
        }

        return this.computeData(data)
    }

    computeData(data) {
        /* given an entity, convert to the computed values for data usage. */
        let r = data

        if(!IT.g(data).is('object')) {
            r = {
                type: data
            }
        }

        return r
    }

    convertLayers(layers, data, results) {
        let r = results;
        if(r==undefined) r = [];


        for (var i = 0; i < layers.length; i++) {
            let aLayer = layers[i];
            let layer = {}
            let InstuctionClass, iLayer;

            if(Instruction.isPrototypeOf(aLayer)) {
                console.log('Found complex Layer')
                InstuctionClass = aLayer;
                iLayer = new InstuctionClass();
                // Call the sub list, resolving first
                // phase.
                let aLayers = iLayer.layers(data)
                // convert to readable
                let sub = [];
                for (var j = 0; j < aLayers.length; j++) {
                    sub.push(this.convertToLayer(aLayers[j], data))
                }
                // add tp existing.
                r = r.concat(sub)
                // add finisher - applying as the _given_ layer.
                aLayer = iLayer.finishLayer()
            }

            // mutate by reference
            this.convertToLayer(aLayer, data, layer)

            r.push(layer)
        }

        return r
    }

    convertToLayer(aLayer, data, layer){
        if(layer == undefined){
            layer = {}
        }

        if(aLayer.func) {

            layer.value = aLayer.func

            if(IT.g(aLayer.func).is('function') ) {
                /* call inline function, expecting array*/
                layer.value = aLayer.func(data)
            }
        }

        if(aLayer.attr) {

            layer.attr = aLayer.attr

            if(IT.g(aLayer.attr).is('function') ) {
                /* call inline function, expecting array*/
                layer.attr = aLayer.attr(data)
            }
        }
        return layer
    }

    set(key, value) {
        /* Set a property on the data of this node. Any attachements are called
        and the layer is recomputed and sent through the pipe to the display canvas.
        If an attachement does not exist, a 'change' event with the key value
        change. */

        // Check for a computed key - add to the correct place in the data.


        this.data[key] = value

        if(this.attachments[key] != undefined) {

            for (var i = 0; i < this.attachments[key].length; i++) {
                let index = this.attachments[key][i]
                // capture the existing attachment, call the compiling
                // layer and push the result.
                //

                // Call the index listed, mixing new results with old.
                let cLayer = this.compiled.layers[index];
                // Resolve the compilation later into a cleaned value.
                // We gete 1 layer here, as the getValue requires a list
                let layer = this.getValue([this.compiled.layers[index]])[0]
                // send the new layer as an index replacement
                this.pipe.send({ change: { key: key, layer, index, id: this.data.id }}, false)

            }
        } else {
            this.pipe.send({ change: { key: value, id: this.data.id }}, false)

        }

    }

    instructions(){
        /* convert for rendering instructions */
        return this
    }
}

class Shape extends CanvasNode {

    actions(){
        return [
            'strokeStyle'
        ]
    }

    defaultConfig(){
        return {
            id: Math.random().toString(32).slice(2)
            // stroke, clear
            , type: 'rect'
        }
    }

    instructions(){
        /* convert for rendering instructions */

        let layers = [
            {
                attach: ['position', 'size']
                , func: (d) => { return [d.type, d.position.concat(d.size)] }
            }
            , Color
            , Stroke
            , instructions.fill
        ]

        return { id: this.data.id, layers };
    }
}

instructions = {}

instructions.fill = {
        /* Perform a fille command */
        attach: []
        , func: ['fill']
}


class Instruction {
    /* A single instruction can replace a layer object within a node.
    The methods provide a neater loadout */
    dataKeys() {
        /* Return a list of keys to collect from the
        main data config

        Other attributes are accessible - but this allows automatic
        detection of keys, and the requirements for preconfig.*/
        let r = {}
        let layers = this.layers()

        for (var i = 0; i < layers.length; i++) {
            if(layers[i].attach){

                for (var j = 0; j < layers[i].attach.length; j++) {
                    r[layers[i].attach[j]] = i
                }
            }
        }

        return Object.keys(r)
    }

    config(){
        /*An instruction maintains its own configuration for building
        a render component.

        Return an array of object and string.

        The object represents the acceptable data format, the seconda argument
        applies the allowed default if the entire data is replaced with a
        single default namespace. */

        /* For the config of this property, the object accepts the 'enabled'
        param. */
        return [{
            enabled: true
        }, 'enabled']
    }

    attach() {
        /* on value set(k, v), the  key(k) may be attached by name to a layer
        for recomputing before sending to the drawing api.
        Each key returned is 'attached'. */
        let dk = this.dataKeys()
        return dk
    }

    defaultConfig(){
        /* defaulted config not applied to the exposed config - used as the
        base for other config merge down. */
        return {}
    }

    computedConfig(data, useCache=true){
        /*return a dictionary as the config built by params with natural defaulting */
        if(useCache === true && this._configCache != undefined){
            return this._configCache
        }


        let r = this.defaultConfig()
        let [config, defName] = this.config()
        let d = data;
        if(data != undefined) {
            if(this.isMutatantConfig(data)) {
                /* push the single value into the defaulted place,*/
                d = {
                    [defName]: data
                }
            }
        }

        Object.assign(r, config, d)

        return r;
    }

    isMutatantConfig(data) {
        /* Check if the given object is a fully-qualified object or a single
        value.
        returns false if not a object {} type.
        returns true if  string, number, array ...*/
        return IT.g(data).is('object') == false
    }

    layers(data){
        if(data == undefined) {
            data = this.computedConfig(data)
        }

        return [this.layer(data)]
    }

    layer(){
        /* Return a ready layer object. */
        return {}
    }

    finishLayer(){
        return {}
    }
}


class Color extends Instruction {

    layer(){
        return {
            attach: ['color']
            , attr: this.fillStyle.bind(this)
        }
    }

    fillStyle(d){
        return ['fillStyle', d.color]
    }

}

class Stroke extends Instruction {

    config(){

        return  [{
            // lineWidth - default (last)
            width: undefined
            // strokeStyle - default (uncchanged)
            , color: undefined
            // pattern CanvasPattern
            , pattern: undefined
            // A CanvasGradient
            , gradient: undefined

            // Mutually exclusive of the color, gradient and pattern.
            // The default object acceptable.
            , style: undefined

            // If a property exists, the stroke is enabled
            // by default. If the stroke object does
            // not exist, the enabled flag is redundant.
            , enabled: true
        }, 'style']
    }

    layer(data){
        return {
            attach: ['stroke']
            , attr: ['strokeWidth', data.width]
        }
    }

}

class RenderLoop  extends DisplayLayer {
    /* manage the call routine of inline elements. */


    update(session){
        /* manage the data routines for the drawing*/
    }

    step(ctx) {

        // Clear
        ctx.clearRect(0,0, this._size.width, this._size.height)

        if(this.rv > this._size.height) {
            this.rv = 0
        }

        this.rv += 1
        let clearVec = [50, this.rv, 20,20]
        // Draw box representing clearing
        ctx.strokeStyle = '#2effa9'
        ctx.strokeRect.apply(ctx, clearVec)
    }

    draw(ctx, session){
        /* write the drawing into the context, after the stepping
        has arranged the update() content accordingly. */
    }

}



lib.mount({CanvasText})
