/*
A Basic logger function for debug messages.
*/


;(function(){
    /* The standard stdout to simulate text to screen without effort.*/
    let stdout = function stdout() {
        console.log.apply(console, arguments)
    }
    requirements = ['console']
    this.global(stdout, requirements)
}).apply(Header)

