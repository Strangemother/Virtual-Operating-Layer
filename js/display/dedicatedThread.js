/* Display dedicated thread. To render the UI and service
graphic write instructions through the pipe. */

importScripts('/js/lib/head.js', '/js/assets.js')
Assets.load('initializeThread')
//Assets.load('system')
Assets.load('drivers')
Assets.load('canvas')

console.log('display thread')

lib.log('Display Apples')

let recv, pipe, icon;

let main = function(){
    recv = new Recv()
}


class Recv {
    /* pipe information given as log text.
    To be parsed and presented to the grapihc thread. */
    constructor() {
        lib.head.pubsub.add('pipe.message', this.message.bind(this))
        this.m_data = this.create.bind(this)

    }

    message(event) {
        console.log('recv', event)

        if(IT.g(event.data).is('string')) {
            let initText = event.data.split('\n')
            if(this.scene) {
                this.scene.update({initText})
            }
        }else{
            let t = event.data.type;
            this[`m_${t}`](event.data)
        }

    }

    create(data) {
        this.scene = new Scene(lib.head.pipe)
        this.m_scene_set(data)
        this.m_data = this.m_scene_set
    }

    m_scene_set(d){
        this.scene.update(d)
    }

    m_start(){
        this.scene.start()
    }
}


class Scene {
    constructor(pipe, initText) {
        /* The new scene should render the active display,
        given text from the logger.*/

        // And transient data given by the display
        this.data = { initText };
        this.pipe = pipe;
        this.createView()
    }

    update(d){
        console.log('updating scene')
        Object.assign(this.data, d)
    }

    movingIcon(){
        let iconNodeDef = {
            color: 'rgb(200, 220,2)'
            , position: [100, 200]
            , size: [10, 10]
            , stroke: {
                // lineWidth - default (last)
                width: 3
                // strokeStyle - default (uncchanged)
                , color: 'red'
            }
        }

        icon = new Shape(iconNodeDef)
        return icon;
    }

    createView() {
        this.icon = this.movingIcon()
        this.start()
    }

    start(){
        let icon = this.icon
        icon.display(this.pipe)

        setInterval(function(){
            icon.set('position', [
                  Math.round(10 + (Math.random() * 600) - 50)
                , Math.round(10 + (Math.random() * 800) - 50)
                ])

        }, 1000)

    }


}


;main()

