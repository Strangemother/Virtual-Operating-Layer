lib.log = function(){
    /* Log messages dispatch though the postMessage. */
    postMessage.apply(self, arguments)
}

onmessage = function(d) {
    console.log('Thread message recv', d)
}
