/*
The first file to provide a head and all assets.
*/
console.debug('first - Define Header Head')

class Header {

    constructor(){

        this.keep = Header.keep.concat([this.constructor.name, 'head',
        'Infinity', 'NaN',  'undefined',  'Object', 'Array',
        'top', 'location',
        'window', 'document', 'Document',
        'chrome'])
        this.store = undefined
        //  this.record = []
        this.instance = this
        console.log('new Header')
    }

    static global(callable, requirements, name){
        /**
         Load a callable unit to the Head, available globally.
         If the head is not defined (pre flight), the function is stored as a 'keep'
         atttribute in the Head init cleanup.

         Provide a list of dependecies as root requirements. They're applied during
         a head load.
         */

        let functionName = name || callable.name
        let items = requirements || []
        items.push(functionName)
        console.debug('Storing global', functionName)

        // this.keep.push.apply(this.keep, items)
        this.keepAdd.apply(this, items)
        //this.record.push([functionName, requirements])
        window[functionName] = callable
    }

    global(callable, requirements, name) {
        return Header.global(callable, requirements, name)
    }

    static chainAppend(name, callable) {
        /* Chain a callable to an existing functional action. */
        console.log('chain Append')
        let f = (function() {
            let internal = this;
            let res = function(){

                let prev = internal.orig.apply(this, arguments);
                let args = Array.from(arguments)
                args.unshift(prev)
                let res = internal.over.apply(this, arguments);
                return res
            }

            //res.name = this.name
            return res
        }).apply({name: name, orig: this.prototype[name], over: callable})
        this.prototype[name] = f
    }

    static keepAdd(/*items*/) {
        /*
         Get the Head() instance (loaded into this.instance) or use the class
         Header.keep.
         */
        let head = this.instance || this
        // merge all the arguments with the keep.
        console.debug('keep', Array.from(arguments))
        head.keep.push.apply(head.keep, arguments)

    }

    getKeep(){
        return this.keep
    }

    wipe() {
        console.log('wipe A')
        this.wipeCore()
        // this.wipeDocument()
    }

    wipeCore(){
        /*
         cleanout the memory and instansiate the head values using the 'keep'
         attribute.
         */
        console.log('Wipe Core')
        let items = []
        let keep = this.keep
        keep = keep.concat(Header.keep)

        Object.getOwnPropertyNames(window).forEach(function(v, x) {
            if(keep.indexOf(v) > -1 ) {
                //console.debug('Skipping', v)
            } else {
                items.push(v)
            }
        });

        let r = {}
        let store = {}
        for(let k of items) {
            try {
                store[k] =  window[k]
                let v = delete window[k]
                r[k] = v;
            } catch(e){
                console.warn('Error', e)
            }

        }
        this.store = store;
        Header.keep = []
        return r
    }

}

Header.keep = []
Header.instance = undefined

var Head = function(){
    /*
    A Callable unit to replace the new Head() function, ensuring
    singleton response.
     */
    console.log('New Head')
    if(this == window) {
        // not 'new'. Return instance or create new.
        if(Header.instance) return Header.instance;
        console.error('Head is not instansiated.')
        return
    }

    // 'new Head', create a new head or return instance.
    if(Header.instance) return Header.instance;

    // Create new
    Header.keepAdd('Head')
    let head = new Header()
    Header.instance = head
    return head
}

