/*
Async events and condition emitters

 */
;(function(){

class AsyncEvents {

    #eventMap = new Map()

    async send(name, data) {
        let eventHandlers = this.#eventMap.get(name)
        if(eventHandlers == undefined) {
            // no event handlers for name.
            console.log('No map for', name)
            return
        }

        for await(const  func  of eventHandlers) {
            await func(data)
        }

        // return Promise.all(
        //     Array.from(eventHandlers.values()).map((caller) => {await caller(data)})
        // )
    }

    getMap() {
        return this.#eventMap
    }

    async on(name, caller) {
        let eventHandlers = this.#eventMap.get(name)
        let setBack = false
        if(eventHandlers == undefined) {
            eventHandlers = []
            setBack = true
        }

        await eventHandlers.push(caller)

        if(setBack) {
            this.#eventMap.set(name, eventHandlers)
        }
    }
}


this.installGlobal(AsyncEvents)


const AsyncFunction = (async () => {}).constructor;
const GeneratorFunction = (function* () {}).constructor;

const isAsyncFunction = value => value instanceof AsyncFunction;
const isGeneratorFunction = value => value instanceof GeneratorFunction;

const isAsync = v => isAsyncFunction(v) || isGeneratorFunction(v)


class Condition {
    /* A Map tracking many keys. When all keys in the map are set
    the condition is true.

    When true an event fires for all hooks. If the _late event_ is enabled,
    and hook applied after the condition is met will automatically fire.

    The condition may refire upon subsequent validations.

        keys = ['a', 'b', 'c']
        let c = new Condition(keys)
        let func = (c)=>console.log('condition met', c)
        c.addHook(func)
        c.set('a', true)
        c.set('b', true)
        c.set('c', true)
        // condition met <c>
        c.addHook(func)
        // condition met <c>

     */
    #keyMap = new Map()

    constructor(keys) {
        this.keys = new Set(keys)
        this.size = keys.length
        this.atomic = 0
        this.handlers = []
        this.match = false
    }

    addHook(func) {
        this.handlers.push(func)
        if(this.match) {
            this.runHook(func)
        }
    }

    set(k, v) {
        if(this.keys.has(k) == false) {
            throw new Error(`Condition is not expecting key ${k}`)
        }

        let t = Boolean(v)
        this.#keyMap.set(k, t)
        this.atomic += Number(t)

        if(this.atomic >= this.size) {
            this.runHooks()

            return true
        }
        return false
    }

    runHook(func) {
        let pfunc = func

        if(!isAsync(func)) {
            pfunc = async ()=>{ func(this) };
        }

        new Promise(func)
    }

    runHooks() {
        new Promise(this.testItems.bind(this))
    }

    async testItems() {
        let e = this.#keyMap
        let trueSize = Array.from(e.values()).reduce((a,b)=>a+b, 0)
        this.atomic = trueSize

        this.match = trueSize == this.size

        if(this.match) {
            for await(const func of this.handlers) {
                await func(this)
            }
        }

    }
}

this.installGlobal(Condition)

}).apply(sessionMemoryLoader())
