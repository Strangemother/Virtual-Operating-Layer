{
    let threadsEnabled = function threadsEnabled() {
        return window.Worker != undefined
    }

    let getConcurrencyCount = function getConcurrencyCount(){
        if(navigator && navigator.hardwareConcurrency) {
            return navigator.hardwareConcurrency
        }

        return 1;
    }

    class Threads {
        constructor(){
            this.psuedo = !threadsEnabled()
        }

        threadPath(){
            return 'js/lib/thread.js'
        }

        createThread(uniqueName){
            /* Produce a new thread (Worker) given the unique
            name as part of the initializer method. */
            return new Thread(uniqueName, this.threadPath());
        }

        createPool(){
            let count = getConcurrencyCount();
            let result = [];

            for (var i = 0; i < count; i++) {
                result.push(this.createThread(i))
            }

            return result
        }

        start(){
            this.pool = this.createPool()
        }
    }


    class Thread {
        constructor(uniqueName, path=undefined) {
            this.uniqueName = uniqueName;
            this.path = path;
            this.mount(path)
        }

        mount(path){
            this.worker = new (this.mainClass())(path);
            this.hook()
        }

        hook(){
            this.worker.onmessage = this.recv.bind(this)
            this.worker.onerror = this.wErr.bind(this)
        }

        mainClass(){
            return Worker
        }

        wErr(e) {
            if(e.type == 'error' && e.path.length == 0) {
                let s = `None descript error from SharedThread "${this.uniqueName}". Is the path correct: (${this.path})?`
                throw new errors.ThreadError(s)
            }
        }

        start(){}

        recv(e){
            lib.log(`Received message on ${this.uniqueName}`)
            system.pubsub.emit({
                name: 'thread.event'
                , data: e
            })
        }

        send(data) {
            this.worker.postMessage(data)
        }
    }


    class SharedThread extends Thread {
        mainClass(){
            return SharedWorker
        }

        hook(){
            super.hook()
            let port = this.worker.port;

            port.onmessage = function(e) {
                // console.log('Message received from worker', e.data);

                lib.log(`SharedThread message: ${e.data}`)
            }

            port.onerror = this.wErr;
            port.onmessageerror = this.wErr
        }

        start(){
            this.threads = new Threads()

        }
    }

    let threadPool = new SharedThread('Interface', `/js/lib/shared-worker.js?cache=${Math.random()}`)


    lib.mount({ threadsEnabled, getConcurrencyCount, threadPool })
}
