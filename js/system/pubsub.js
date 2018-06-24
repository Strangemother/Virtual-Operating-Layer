/*
a subscribable message routine through the system allows publisher/subscriber
 */
{

let getID = function(){ return Math.random().toString(32).slice(4); };
var PM = {}

class SubscriptionCore {
    /* read messages through the core dispatch routine. */
    constructor(){
        lib.log('new SubscriptionCore')
        this.id = getID()
        this._own = 0
        PM[this.id] = {}
    }

    single(name, onefunc){
        /* subscribe to an event with a function - if the
        event name exists, the listener is not applied.

        This is useful for resetting the same listener without concern.
        ensuring only 1 _add()_ call is applied to the event `name`

            system.pubsub.single('one', function(){ console.log('a') })
            "1e3nbfbag"
            system.pubsub.single('one', function(){ console.log('b') })
            "1e3nbfbag"
            system.pubsub.emit('one')
            a
        */
        if(this.has(name) == false) {
            return this.add(name, onefunc)
        }

        // else return the natural id
        return this.getIds(name)[0]
    }

    getIds(name){
        /*  returna list of registered evenr handler IDs for a given event name.
        */
       if(PM[this.id][name] == undefined) {
            return []
       }

       return Object.keys(PM[this.id][name])

    }

    has(name) {
        /*return true if the event name is registered else false */
        return PM[this.id][name] != undefined

    }

    add(name, func){
        /* subscribe to a ame with a function. Return the listener id. */
        if(PM[this.id][name] == undefined){
            PM[this.id][name] = {}
        }

        let id = getID()
        PM[this.id][name][id] = func;
        this._own += 1
        this.emit('SubscriptionCore.add', {id, eventName:name})
        lib.log('Add new subscriber', name, id)
        return id;
    }

    remove(key) {
        /* remove elements from the public scope by function name,
        subscriptioncore name or event name.
        returns a count of removed listeners */
        let calls = 0;

        for(let subCoreID in PM) {
            if(subCoreID == key) {
                this.emit('SubscriptionCore.deleted', {key})
                delete PM[subCoreID]
                return 1
            }

            let items = PM[subCoreID]

            for(let eventName in items) {
                if(key == eventName) {
                    delete items[eventName]
                    return 1
                }

                let funcs = items[eventName]
                let keys = Object.keys(funcs);
                if(keys.indexOf(key)>-1) {
                    this._own -= 1
                    lib.log(`Deleting ${key}`)
                    delete funcs[key]
                    this.emit('SubscriptionCore.deleted', {eventName, key})
                    calls += 1
                }

            }
        }

        return calls;
    }

    emit(name, data) {
        if(arguments.length == 1 && typeof(name) != 'string') {
            data = name;
            name = data.name;
        };

        let calls = 0
        let anyE = PM[this.id]['*']
        for(let _id in anyE) {
            anyE[_id](name, data)
            calls += 1
        }

        for(let subCoreID in PM) {
            let items = PM[subCoreID]
            for(let funcID in items[name]) {
                let func = items[name][funcID]
                if(func == undefined) {
                    lib.warn('DEAD pubsub method', funcID)

                    continue
                }

                if(calls == 0) {
                    lib.log('SubscriptionCore.emit', name)
                }

                func(data);
                calls += 1
            }
        }

        return calls;
    }

    getPublishScope(name){
        let pm = PM[this.id];
        if(name == undefined) {
            return pm;
        }
        return pm[name]
    }
}


lib.mount({ SubscriptionCore })

// lib.SubscriptionCore = SubscriptionCore

}
