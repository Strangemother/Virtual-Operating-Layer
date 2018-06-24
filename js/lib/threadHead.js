{

lib.log = function(){
    /* Log messages dispatch though the postMessage. */
    let d = Array.from(arguments)
    try {
        postMessage.apply(self, d)
    } catch(e) {
        if(e instanceof(TypeError)) {
            console.log('Bad Type', d)
        }
    }
}


let main = function(){
    lib.head = new ThreadHead()
}

onmessage = function(d) {
    console.log('Thread message recv', d)
}

var onmessageSubscriptionCore = new lib.SubscriptionCore

var _onmessageFunctionalHandler = function(d){
    console.log('Emit thread message', d)
    onmessageSubscriptionCore.emit('message', d)
}

if(onmessage != _onmessageFunctionalHandler) {
    onmessage = _onmessageFunctionalHandler;
}

class ThreadHead {
    constructor(){
        this.pubsub = onmessageSubscriptionCore
        this.hookOnmessage()
    }

    hookOnmessage(){
        console.log('ThreadHead onmessage ready')

        this.pubsub.add('message', this.message.bind(this))

        let pipe = new Pipe(postMessage)
        onmessageSubscriptionCore.add('message', pipe.onmessage.bind(pipe))
        this.pipe = pipe;
    }

    bindStandardFunction(){

    }

    message(data) {
        console.log('message threadHead', data)
    }

    post(data) {
        this.pipe.send(data)
    }
}



class Pipe {
    /* A single pipe provides communication through threads.
    Encoder and decoder, data switching.
    */
    constructor(postCallback, encoding='utf-8'){
        this.postCallback = postCallback
        this.encoder = new TextEncoder(encoding)
        this.decoder = new TextDecoder(encoding)
    }

    send(data, encode){
        /* send informatio through the pipe to no explicit receiver.
        Text encoding by default.*/
        // console.log('Post and send')
        if(encode == false) {
            return this.postCallback.call(self, data)

        }
        let d = this.encoder.encode(data)
        this.postCallback.call(self, d, [d.buffer])
    }

    onmessage(data) {
        /*  recevier bound to the thread inbound functional caller. */
        let d = data.data
        if(data.data instanceof ArrayBuffer) {
            d = this.decoder.decode(data.data)
        }
        console.log('pipe onmessage')
        onmessageSubscriptionCore.emit('pipe.message', { data:d })
    }

}


/* A Type map */

;main();
}
