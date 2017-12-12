onconnect = function(e) {
    var port = e.ports[0];

    port.onmessage = function(e) {
        var workerResult = 'Result: ' + (e.data[0] * e.data[1]);
        port.postMessage(workerResult);
    }

    port.postMessage('connect')

    importScripts('./head.js', '../files.js')
    Assets.load('initializeThread')
    console.log('sharedthread')

    lib.log('Apples')

}
