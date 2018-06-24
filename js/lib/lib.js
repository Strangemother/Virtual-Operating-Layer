/* Elements under the boot. */
{
/* All application constant definitions */
const LIB_VERSION = 0.1

let logger = function(){
    if(self['document'] == undefined) {
        self['document'] = Assets.document()
    };

    let _libcoreLogger = self['document'].getElementsByTagName('libcore')[0]
    if(_libcoreLogger == undefined) {
        return {
            log(){}
        }
    };

    return (function(){
        let logger = _libcoreLogger;
        return {
            log(){
                let r = ['\n']
                for (var i = 0; i < arguments.length; i++) {
                    r.push(arguments[i])
                    r.push(' ')
                }

                logger.append.apply(logger, r)
            }
            , el: logger
        }
    })()
}

class Lib {

    constructor(){
        this.it = IT.g;
        this._logger = logger()
    }

    log(){
        this._logger.log.apply(this, arguments)
    }

    warn(){
        console.warn.apply(console, arguments)
    }

    initializeSystem(){
        this.log('Start')
        this.boot = Boot.run()
    }

    mount(entity, name) {
        /* Provide an object or function to load into the library as a
        callable method.*/
        if(this.it(entity).is('object')) {
            for(let key in entity) {
                this.mountFunction(entity[key], key)
            }

            return
        }

        this.mountFunction(entity, name)

        return
    }

    expose(entity, name) {
        /* Expose the given object or function to the _global_ space.
        The entity is accessible outside of the lib - within the app scope.

        each file closure will mount or expose the value. Depending upon
        env setup the mount may expose the entity though self, {export} or
        _globalise_ into the scope.
        */

         if(this.it(entity).is('object')) {
            for(let key in entity) {
                this.exposeFunction(entity[key], key)
            }

            return
        }

        this.exposeFunction(entity, name)
    }

    getLibInstance(){
        /* return an active lib instance, containing all functions
        accessible across all closures.*/
        return this;
    }

    mountFunction(func, name) {
        /* Add a function to the library for other file closures to access
        through 'lib' */

        if(name == undefined) {
            name = func.name;
        }

        // no name is unmountable.
        if(name == undefined) {
            let s = `A mounting function needs a name`
            throw (new errors.MountError(s))
            return false;
        }

        let lib = this.getLibInstance()

        if(lib[name] != undefined) {
            // Check for existance, fail early if not.
            if(this.allowMountOverride()) {
                this.warn(`Remounting ${name}`)
            } else {
                let s = `Cannot remount function ${name}`
                throw (new errors.MountError(s))
                return false;
            }
        }

        lib[name] = func;

        return true;
    }

    allowMountOverride(){
        return false
    }

    exposeFunction(func, name) {

        if(name == undefined) {
            name = func.name;
        }

        // no name is unmountable.
        if(name == undefined) {
            let s = `An exposing function needs a name`
            throw (new errors.MountError(s))
            return false;
        }

        self[name] = func
        return true
    }

    getGlobals(item){
        return Object.keys(item)
    }

    globals(against){
        let _gl = against || self['STATIC_HEAD'] || this._globals;

        let sortf = function(aa){
            let id = _gl.indexOf(aa);

            if(id == -1){
                e.push(aa)
                return true
            };

            return false;
        };
        let e= []
        let g = this.getGlobals(self);
        let l = g.filter(sortf)
        return e
    }
}

//console.log('export lib', self)
// export initFunc

self.lib = new Lib
self.lib._globals = self.lib.getGlobals(self)
}
