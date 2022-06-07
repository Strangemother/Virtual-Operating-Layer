let bus = undefined;

let main = function(){
    bus = new Bus()
    window.addEventListener('DOMContentLoaded', (e)=> bus.emit('ready'))
    bus.on('ready', (d)=>readyEvent())
}


let readyEvent = function(){
    console.log('customPointer')
    customPointer()
let ir = new Iris('.iris')

}


const template = function(){
    return document.querySelector('.winbox').cloneNode(true)

}

const spawn = function(title="Custom Root"){
    let windowContainer = document.querySelector('.panels')
    return new WinBox(title, {
        root: windowContainer
    });
}


;main();
