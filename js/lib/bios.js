/*

basic input output loading for the configurations and the head and assets.


The First file for browser interface loading - containing HTML interface
build and core configuration load.

This tooling is unique to the build export requirements, providing the base
for interfacing with the developed application.

In a node app, the buildout is CLI defined. In ASM, this woud be a screen interface base.
Base settings are frozen into the _compiled_ unit. Application definitions are
defined in the config.
 */
{
    //var enc = new TextEncoder("utf-8").encode
    const ICO = {
        SELECTED: undefined,
        ANNOUNCE: 1,
        // int value for seconds waiting until continue after announcement
        // without response.
        ANNOUNCE_WAIT: 10,
        EXE_ORDER: [
            /* Basic running eith visual connection*/
            'BIOS',
            /* Custom loadout full of OS build config.*/
            'ICO',
            /* Implement initial code, Assets and boot source.*/
            'HEAD',
            /* Download additional.*/
            'ASSETS',
            /* Initialize the system, continuing the basic loadout*/
            'INIT',
        ]
    }

    const SYS = {
        STATE: -1
        , HIAO_FG: '#4ac54a'
        , HIAO_BG: '#222222'
        , HIAO_SZ: '1.1em'
        , HEAD: 'js/lib/head.js'
        , ASSETS: "js/assets.js"
    }

    /* replaced by ISO-VOL throughput after VOL binding. */
    let DATA = {}

    let EXECUTE = function(){
        HAIO.attached.stdOut('No BIOS to EXECUTE')
    }

    let main = function(){
        let _executeHandler = function(e){
            removeEventListener('EXECUTE', _executeHandler);
            executeHandler(e)
        };
        addEventListener('EXECUTE', _executeHandler)
        EXECUTE = new BIOS(document)(ICO)
        dispatchEvent(new CustomEvent('BOOT', {
            detail: {
                ICO: ICO
            }
        }))
    }


    let executeHandler = (function(){


        let eventListener = function(e){
            // BIOS.execution()

            let bios = EXECUTE();

            // should the host interface changes be deleted.
            // if true, the host setup() (html) is removed.
            let unprint = false;

            return;

            setTimeout(function(){
                bios.stdOut('Perform simulated shutdown')
                bios.shutdown(unprint)
            }, 1000)
        }

        return eventListener;

    })()

    class VOL_ISO {
        /* A Virtual Operating layer - connecting the base operations
        of the FIOU and maybe the BIOS to the isomorphic layer.

        In a web context, this may be events. In an VOL container, the
        VOL service has applied announcement connectioned.

        Security allows only a few operationd from the bios - in order.*/

        constructor(ico){
            /* A new VOL ISO may announce depending on the ICO */
            // ICO announcement may be off for security.
            if(ico.ANNOUNCE>0) {
                // Send an alert, wait for return.
                HAIO.attached.stdOut(`VOL_ISO::Announce`)
                dispatchEvent(new CustomEvent('VOL_ISO',
                    {
                        detail: {
                            timestamp: +(new Date)
                            , id: Math.random().toString(32).slice(2)
                        }
                    })
                )
                //VOL.announce(ico)
                if(ico.ANNOUNCE_WAIT>0){
                    HAIO.attached.stdOut(`VOL_ISO::Wait for response...`)
                }

                BIOS.system_wait(ico.ANNOUNCE_WAIT, 5)
            }
        }
    }

    // Fundamental Input Output Unit
    class FIOU {

        static tty(){
            console.log.apply(console, arguments)
        }

        static system_wait(message, timeout, can_interupt) {
            /* Halt any inline BIOS processing until the wait clears.
            message     The print to display before halting
            timeout     Seconds before normal operations resume.
            can_interupt    If the operation can be canceled.*/

            if(message != undefined) {
                this.tty(message)
            }

            DATA.WAIT = true

            DATA.WAIT_TIMER = setTimeout(function() {
                this.tty('continue wait')
                DATA.WAIT = false
                delete DATA.WAIT_TIMER
            }.bind(this), timeout * 1000);

        }

        // initial configuration object
        static loadICO(config){
            FIOU.tty('freeze ico')
            Object.freeze(config)
            Object.seal(config)
            Object.preventExtensions(config)

            this.ICO = config
            return config;
        }
    }

    // Host attached interface outout
    class HAIO {

        static attach(owner) {

            // Perform 'headless' attachement; giving an 'owner' (the document)
            // to _a_ setup, pproducing a host connected interface.
            let h = (new HAIO)
            let vdu = h.setup(owner)
            // bind the given host to the headless setup
            h.vdu = vdu;
            h.owner = owner;
            // Hardset the printing typemap
            h.typemap = HAIO.print_typemap()
            // First printout.
            h.stdOut('HAIO::Attached Host interface')
            HAIO.attached = h

            return h;
        }

        static print_typemap(){
            return {
                string: (s) => (`${s} `)
                , object: (s) => (JSON.stringify(s) + ' ')
                , boolean: this.string
            }

        }

        static destroy(unprint=false){
            let h = HAIO.attached;
            let timeout = 1500;
            h.stdOut(`HAIO::Destroy HAIO in: ${timeout / 1000} seconds`)
            setTimeout(function(){
                h.destroy(unprint)
                h.stdOut('HAIO::Killed HAIO')
            }, timeout)
        }

        destroy(unprint=false){
            this.stdOut('HAIO::Destroying self.')

            if(unprint == true) {
                this.stdOut('HAIO::Deleting UI. End.')
                this.owner.getElementById('HAIO::2').remove()
                this.owner.getElementById('HAIO::1').remove()
            }

            delete this.vdu
            delete this.typemap
            delete this.owner
            this.stdOut = FIOU.tty.bind(FIOU)
        }

        setup(owner) {
            /*

             */
            let create = owner.createElement.bind(owner);
            let style = create('style');
            style.id = 'HAIO::1'
            let vduElement = create('libcore');
            vduElement.id = 'HAIO::2'

            style.innerHTML = `body { background: ${SYS.HIAO_BG}; }
                libcore { color: ${SYS.HIAO_FG};; font-family: monospace; font-size: ${SYS.HIAO_SZ};
                white-space: pre; margin: 0 2em; display: block; }`

            owner.head.appendChild(style);
            owner.body.appendChild(vduElement);
            let _app = vduElement.append

            vduElement.append = function(){

                let r = _app.apply(vduElement, arguments);

                if(self['document']) {
                    document.scrollingElement.scrollTop = document.scrollingElement.scrollHeight
                }

                return r;
            }

            return vduElement
        }

        stdOut() {
            let typemap = this.typemap
            for(let s of arguments) {
                let f = typemap[typeof s];
                if(f == undefined) { f = typemap.string }
                this.write(f(s))
            }
            this.write('\n')
        }

        stdSrc(path, loadStack, owner, async=true, onload=undefined) {
            if(owner == undefined) {
                owner = this.owner;
            }

            let s = owner.createElement('script')
            s.src = path;
            s.async = async
            this.stdOut(`stdSrc::${path}::async(${async})`)
            //s.onreadystatechange
            loadStack[s.src] = false;
            let _this = this;
            s.onload = function(e){
                if(e.type === 'load') {
                    loadStack[this.src] = true
                    if(onload != undefined) {
                        onload(e)
                    }
                    // _this.stdOut(_this.loadStack)
                }
            }

            owner.body.appendChild(s)
            return s;
        }

        stdKeep(k, v){
            this.stdOut(`HAIO::stdKeep`, k , v)
            DATA[k] = v;
        }

        stdRead(v) {
            let s = DATA;
            if(s[k] == undefined){
                s = SYS;
            };

            let r = s[k]

            if(r == undefined) {
                this.stdOut(`HAIO::stdRead key ${k} failure`)
            }

            return r
        }

        write(line) {
            this.vdu.append(line)
        }
    }


    class BIOS extends FIOU {

        constructor(hostOwner){
            super()
            DATA.haltKill = false;
            DATA.WAIT = false;
            //this.stdOut = this.tty;
            this.attachHAIO(hostOwner)


            return this.initialize.bind(this)
        }

        initialize(ico){
            /* Initial command called by the booting facilitator, start the
            initial provess; All configurations are expected null. */
            this.stdOut('BIOS::ICO execution')
            addEventListener('IMMEDIATE_RESPONSE', this.immediateResponseHandler.bind(this))

            // return active biod;
            return this.execute.bind(this)
            //let owner = this.haio.owner;
        }


        get_ICO(){
            return DATA.ICO || ICO
        }

        execute(index=0) {
            this.stdOut('BIOS::Execute. Reset EXECUTE_INDEX.')
            DATA.EXECUTE_INDEX = index;
            this.executeNext()
        }

        executeNext(ico){
            ico = ico == undefined? this.get_ICO(): ico;
            let index = DATA.EXECUTE_INDEX;
            if(index < ico.EXE_ORDER.length) {
                this.executeStep(ico.EXE_ORDER[index], ico)
                if(DATA.WAIT == false) {
                    this.stdOut('... Natural continue from next execution')
                    this.executeNext(ico)
                }
            }
        }

        executeStep(name, ico) {
            if(DATA.WAIT == true) {
                this.stdKeep('NEXT', name)
            } else {
                this.stdOut(`\nBIOS::EXECUTE (${DATA.EXECUTE_INDEX+1}/${ico.EXE_ORDER.length}) ${name}...`)
                this[`execute${name}`](ico)
                DATA.EXECUTE_INDEX += 1
            }
        }

        executeBIOS(ico) {
            // announce?
            // load sys modules after loadout.
            // this.vol = new VOL_ISO(ico)
            this.announceWait(ico, undefined, this.continue_BIOS.bind(this))
        }

        dispatchExecutionEvent(name, id){
            // this.stdOut(`Announce ${name}`)
            id = id != undefined? id: Math.random().toString(32).slice(2);

            dispatchEvent(new CustomEvent(name || 'EXE_BIOS',
                {
                    detail: {
                        timestamp: +(new Date)
                        , id: id
                    }
                })
            )
            return id;
        }

        announceWait(ico, name, callback){
            DATA.WAIT = true
            if(ico.ANNOUNCE>0) {
                // Send an alert, wait for return.
                let id = Math.random().toString(32).slice(2);
                DATA.WAIT_ID = id
                this.dispatchExecutionEvent(name, id)

                if(DATA.WAIT_SKIP == true) {

                    DATA.WAIT_SKIP = false;
                    DATA.WAIT = false
                    DATA.WAIT_ID = undefined

                    callback()
                    return
                }

                //VOL.announce(ico)
                if(ico.ANNOUNCE_WAIT>0){
                    let seconds = ico.ANNOUNCE_WAIT
                    let s = `EXE_BIOS::Wait for response (${seconds} Seconds)`
                    this.wait_execution(s, seconds, callback)
                }
            }
        }

        wait_execution(message, timeout, callback) {
            /* Halt any inline BIOS processing until the wait clears.
            message     The print to display before halting
            timeout     Seconds before normal operations resume.
            */

            if(message != undefined) {
                this.stdOut(message)
            }

            DATA.WAIT = true

            let f = (function(callback){
                return function(data){
                    DATA.NEXT = undefined
                    DATA.WAIT = false
                    this.continue_execution(callback, data)
                }.bind(this)
            }).call(this, callback)

            DATA.NEXT = f;

            DATA.WAIT_TIMER = (function(timeout, callback){
                return setTimeout(function() {
                    this.stdOut('Wait timeout. Continue...')
                    callback()
                }.bind(this), timeout * 1000);
            }).call(this, timeout, f)
        }

        immediateResponseHandler(e) {
            let id = e.detail.id;
            // this.stdOut(`Received IMMEDIATE_RESPONSE ${id}`, DATA.WAIT_ID)
            if(id == DATA.WAIT_ID) {

                clearTimeout(DATA.WAIT_TIMER)
                delete DATA.WAIT_TIMER
                this.finish_wait(e.detail.data)
            }
        }

        finish_wait(data) {
            if(DATA.WAIT == false) {
                console.warn('Wait Finish called, but BIOS is not waiting.')
                return false;
            }

            if(DATA.NEXT == undefined) {
                DATA.WAIT_SKIP = true
                // console.error('Wait finish missing DATA.NEXT')
                return false;
            }

            let next = DATA.NEXT;
            delete DATA.NEXT;
            next(data)
        }

        continue_execution(last_callback, data){
            // this.stdOut('Continue execution')
            DATA.WAIT = false
            delete DATA.WAIT_TIMER
            if(last_callback) {
                //this.stdOut('Performing continue:', last_callback.name)
                last_callback(data)
            }

            this.executeNext()
        }

        executeICO(ico){
            /* Called by the previoud stage (the execution), this function
            loads the chosen ico after announce or execute/load. */
            this.stdOut('Load::ICO Config')
            if(ico.SELECTED != undefined) {
                this.stdSrc(ico.SELECTED, this.loadStack);
            } else {
                this.stdOut('BIOS::ICO.SELECTED missing.')
                this.stdKeep('CHOOSE_ICO', true)
            }
        }

        executeHEAD(ico){
            /* Execute the main application requirements, loading source
            files and assets to install. Follow with '*/
            this.announceWait(ico, 'HEAD', this.continue_HEAD.bind(this))
        }

        executeASSETS(ico){
            this.announceWait(ico, 'ASSETS', this.continue_ASSETS.bind(this))
        }

        continue_BIOS(ico_updates){
            // Perform any BIOS actions - changing execution orders.
            let ico = Object.assign(this.get_ICO(), ico_updates)
            DATA.ICO = BIOS.loadICO(ico)
        }

        continue_HEAD(d){

            this.stdOut('Load::SYS HEAD')
            Object.assign(SYS, d)
            this.stdSrc(SYS.HEAD, this.loadStack, undefined, false);
        }

        continue_ASSETS(d){
            DATA.ASSETS_LOADED = false

            let sd = {
                loadset: 'initial'
                , funcName: 'initializeSystem'
                , assets: SYS.ASSETS
            };

            Object.assign(sd, d)

            let onload = function(){

                try {
                    this.stdOut('Assets:', Assets != undefined);
                    DATA.ASSETS_LOADED = true
                    Assets.load(sd.loadset, function(){
                        self[sd.funcName]()
                    })

                } catch(e){
                    if(e instanceof ReferenceError){
                        this.stdOut('Asset failure', SYS.ASSETS, e);
                    }
                    console.error(e)
                }


            }.bind(this)

            let s = this.stdSrc(sd.assets, this.loadStack, undefined, false, onload);
            return this
        }

        executeINIT(ico) {
            this.stdOut('\nINIT EXECUTE')
            this.announceWait(ico, 'INIT', this.continue_INIT.bind(this))
        }

        continue_INIT(){
            this.stdOut('\nINIT continue')
            this.dispatchExecutionEvent('OFFLOAD')
        }

        destroy(unprint=false){
            this.detachHAIO()
            HAIO.destroy(unprint)
        }

        shutdown(unprint=false, timeout=1000) {
            /* Perform BIOD close, destroying internal information and connection
            to the host interface.
            If haltKill is true when the grace period expires, shutdown is aborted.*/
            this.stdOut(`BIOS::Shutdown. Grace: ${timeout/1000} second${timeout == 1000? '': 's'}`)

            // perform destroy grace.
            setTimeout(function(){
                if(DATA.haltKill == false) {
                    this.stdOut('BIOS::Perform destroy')
                    this.destroy(unprint)
                } else {
                    this.stdOut('BIOD::halt kill flag. Shutdown aborted.')
                }
            }.bind(this), timeout)
        }

        attachHAIO(hostOwner) {
            let haio = HAIO.attach(hostOwner);
            // A location to store the state of loading sources.
            this.loadStack = {}
            this.stdOut = haio.stdOut.bind(haio);
            this.stdSrc = haio.stdSrc.bind(haio);
            this.stdKeep = haio.stdKeep.bind(haio);
        }

        detachHAIO(){
            let h = HAIO.attached;
            this.stdOut('HAIO::Detaching')
            this.stdOut = FIOU.tty
            delete this.stdSrc;
            delete this.loadStack;
            this.stdOut('HAIO::Detached')
        }

        stackIsLoaded(){
            /* Return boolean value. True if all elements within the
            loadStack are loaded, false if one or more items is loading. */
            let ss = new Set(Object.values(this.loadStack))
            return ss.size == 1 && ss.has(true)
        }

        executeStack(){
            return (this.stackIsLoaded() && SYS.execute == 1)
        }
    }

    main()

}
