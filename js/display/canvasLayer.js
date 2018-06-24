{
/* A Canvas layer defines a drawable space for any rendering unit -
such as a Screen.

The drawing loop ticks a function.*/

class CanvasLayer extends DisplayLayer {
    /* An extraction of the display unit to render view items. */

    static id(){
        /* return a unique ID for this driver, used for
        memory mapping*/
        return `layer.Canvas`
    }

    init(){
        /* Tell the system a new screen has attached. */
        system.pubsub.emit(`${this.id()}.init`, {
            id: this.id()
        })
    }

    screenLoad(screen){
        /* make UI layer, start app, begin processing - no rendering yet. */
        lib.log(`Mount layer "${this.id()}" to "${screen.id()}"`)

        let el = document.createElement('canvas')
        el.id = this.id()

        let space = new lib.CanvasRenderLoop({
            canvas: el
            , fps: 120
        })

        this.space = space;
        lib.log('Loaded canvas view. Ready to render.')
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
        let color = 'black'
        document.body.append(el)

        let size = this.getSize()
        el.width = size.width - (borderWidth * 2)
        el.height = size.height - (borderWidth * 2)

        let cssEl = document.createElement('style');
        cssEl.id = `${this.id()}.style`
        cssEl.innerHTML = `canvas { border: solid ${borderWidth}px ${color}; top: 0px; left: 0px; position: fixed; }
        body { margin: 0; overflow: hidden}`
        document.body.append(cssEl)
        window.scrollTo(0,0)
    }
}

let fps = 0, tickI = 0, avgFPS=0
let lastD = +(new Date);
let viewFPS = 0;

let drawFPS = function(ctx, drawRate){

    if(!lastD) {
     lastD = Date.now();
     fps = 0;
     return;
    }

    let delta = (Date.now() - lastD)/1000;
    lastD = Date.now();
    fps = 1/delta;
    if(tickI % drawRate == 0) {
        viewFPS = Math.round(fps)
        tickI = 0;
    }

    tickI++

    // Clear
    let clearVec = [0, 0, 40, 30]
    ctx.clearRect.apply(ctx, clearVec)

    // Draw text
    ctx.fillStyle = '#2effa9'
    ctx.font = '16px monospace'
    ctx.fillText(viewFPS, 10, 20)

    // Draw box representing clearing
    ctx.strokeStyle = '#2effa9'
    ctx.strokeRect.apply(ctx, clearVec)
}

let drawFunction = function(ctx){
    drawFPS(ctx, 20)
}

let CanvasRenderLoop = function(config){
    'use strict'

    var listen = window['addEventListener'] ? window.addEventListener: window.attachEvent
        , scripts = document.getElementsByTagName("script")
        , script = scripts[scripts.length - 1]
        , core, spindle, utils, space = {}
        , self = this
        ;

    var setup = function(){
        config.id = Math.random().toString(32).slice(6)
        space.draw = draw;
        space.drawFPS = drawFPS;

        space.create = create;
        space.config = config;

        space.inspectCanvas = inspectCanvas;
        space.getCanvas = getCanvas;
        space.animFrame = animFrame;
        space.calcWidth = calcWidth;

        console.log('Setup', config.name || config.id);
        return space
    }

    var ready = function(cotton){
        window.dispatchEvent(new CustomEvent('canvas:ready'))
        calcWidth(getCanvas())
        console.log('Im good to go', config.name || config.id);
    }

    var calcWidth = function(canvas){

        var width = canvas.clientWidth * (window.devicePixelRatio);
        var height = canvas.clientHeight * (window.devicePixelRatio);
        canvas.width = width;
        canvas.height = height;
        return {
            width: width
            , height: height
        }
    }

    /**
     * The `draw()` method is the cheapest method to run your canvas code.
     * Optionally provide a `canvas` String or Node and a required draw method.
     *
     * If the canvas is omited, Cotton will default to the `canvas#main` from the
     * DOM.
     *
     * If no draw method is supplied. The basic stage display is provided.
     *
     * @param  {[type]} draw [description]
     * @return {[type]}      [description]
     */
    var draw = function(canvas, draw) {
        var f = draw;
        if( arguments.length == 1
            && it(canvas).is('function') ) {
            f = canvas;
            canvas = undefined;
        };

        var cnv = create(canvas, f);
        space.context = cnv
        cnv.animFrame.loop()
        return cnv
    }

    var create = function(canvas, callback) {
        /*
         run the method of execution on a canvas, wrapping the
         canvas with CottonDuck
         */
        var insp = inspectCanvas(canvas);
        insp.animFrame = animFrame(insp.context, callback);
        return insp;
    }

    var inspectCanvas = function(canvas) {

        var cnv = getCanvas(canvas);
        var dpr = window.devicePixelRatio || 1;
        var ret = {
            context: undefined
            , canvas: cnv
            , width:  0
            , height: 0
            , devicePixelRatio: dpr
        };

        ret.context = cnv.getContext("2d");
        // debugger;
        ret.context.scale(dpr, dpr);
        // this.step.start(1000, context);

        var c = calcWidth( cnv)
        ret.width = c.width  * dpr;
        ret.height = c.height * dpr;
        return ret;
    }

    var getCanvas = function(canvas){
        /*
         Return a canvas element, peoviding a string, ID or canvas item.
         IF one canvas exists this is returned.

         Order of preference:

            Canvas element
            Canvas Element ID
            Canvas Element 1 found
         */

        if( canvas === undefined ) {
            // find elements

            if(config.canvas != undefined) {
                return config.canvas;
            };

            var els = document.getElementsByTagName('canvas');
            if(els.length == 1) {
                canvas = els[0];
            };

        } else {
            var canvasStr;

            if( it(canvas).is('string') ){
                // by idl
                canvasStr = canvas;
                canvas = document.getElementById(canvasStr)
            } else if( canvas instanceof HTMLElement ) {
                // By element
            } else {
                return false
            }

        }

        if( (canvas instanceof HTMLElement) != true ) {
            throw new Error('Canvas:'  + canvas + ' must be HTML element')
        }

        return canvas;
    }

    var animFrame = function(context, callback){
        var renderFunction = function(){};
        var run = true;
        var r = {
            loop: undefined
            , render: undefined
            , run: run
            , start: undefined
            , stop: undefined
            , context: context

        }

        r.setRenderfunction = function(f){
            renderFunction = f
        }

        r.render = function render(callback){
            if(callback) { renderFunction = callback; };

            return renderFunction;
        };

        r.frame = function frame() {
            renderFunction(r.context)
        }

        var browserAnimationFrame = (function(){
            return window.requestAnimationFrame      ||
                  window.webkitRequestAnimationFrame ||
                  window.mozRequestAnimationFrame    ||
                  window.oRequestAnimationFrame      ||
                  window.msRequestAnimationFrame     ||
                  function(/* function */ callback, /* DOMElement */ element){
                      window.setTimeout(callback, config.fps);
                  };
        })();

        r.loop = function() {
            r.createTime = +(new Date);
            var _loop = function(){
                (function animloop(){
                    r.run && browserAnimationFrame(animloop);
                    r.frame()
                })();
            };
            _loop();
        };


        r.start = function(){
            r.run = true;
            r.loop()
        }

        r.stop = function(){
            r.run = false;
        };

        r.running = function(){
            return r.run
        }

        if(callback !== undefined) {
            renderFunction = callback;
        };


        return r;
    }

    var main = (function(){

        space = setup()
        ready()

        return space;
    }).call(this);

    return main;
}


lib.mountFunction(CanvasRenderLoop)
lib.mount({[CanvasLayer.id()]:CanvasLayer})

}
