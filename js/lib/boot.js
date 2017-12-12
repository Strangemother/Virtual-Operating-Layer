/* first file called by initial */

lib.log('boot')

class Boot {
    static run() {
        /* First function to call. called by procedd "initializeSystem" */
        lib.log('run')
        return (new this)
    }

    constructor() {
        this._threaded = this.threads()
        lib.log('Threaded:', this._threaded)
        Assets.load('boot', this.assetsLoaded)
    }

    assetsLoaded(d){
        console.log('boot.')
    }

    threads(){
        if(lib.threads == undefined) {
            return -1
        }

        try {
            lib.threads.start()
            return 1;
        } catch(e) {

            if(e.code == 18) {
                lib.warn(e.name, 'psuedo threading enabled')
                lib.threads.psuedo = true;
                return 0
            } else {
                console.error(e)
            }

            let _errors = lib.errors || self['errors'];

            if(_errors != undefined) {
                throw (new _errors.ThreadError(e))
            }

            return -1
        }

    }
}

self.initializeSystem = function(){
    let v = lib.initializeSystem.apply(lib, arguments);
    delete self.initializeSystem;
    return v
}

lib.log('ready')
