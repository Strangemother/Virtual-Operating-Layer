/* System boot. Loading interface, broadcast and threaded services*/
{


let Lib = lib.constructor;

INIT_SYSTEM_MEMORY = {

    // IDS of allowed memory modules.
    ids: [
        'base.memory'
        , 'base.Keyboard'
        // Notice the display doesn't have a base.* taxonomy.
        // This is because the Dispay loaded modules will complete
        // the namespace.
        , 'Display'
    ]

    // Data loaded into incoming driver.
   , 'base.memory': {
        cake: 'foo'
    }

    , display: {
        auto: true
        , interfaceSuite: 'foo'
    }

    // Settings for the screen setup and screen manager.
    , DisplayScreen: {
        // Name of a display, loading modules as layers
        root: {

            // Each driver layer to load into the named DS.
            layers: [
                'layer.Canvas'
            ]

            // layer managers
            , interface: [
                'Interface'
            ]
        }

        // Cusom config of the root layer when loaded into a 'root'
        // display screen. Is merged on top of
        // INIT_SYSTEM_MEMORY['Interface.root']
        , 'Interface.root': {

            // Any assets extending the layers.
            // implements: [
            // ]

            /*Method to run when the interface is loaded. */
            start: 'defaultStart'
        }
    }


    // _Locked_ configuration of the Interface, with a 'root'
    // DisplayScreen config.
    // Merged with custom layer info
    , 'Interface.root': {
        implements: [
            'layer.CanvasText'
        ]
    }
}

SYSTEM_DRIVERS = {}

class System extends Lib {
    constructor(){
        super()
        lib.log('system')
        this.load()
    }

    load(){
        Assets.load(FILES.system, this.onLoaded.bind(this))
    }

    onLoaded(){
        console.log('Loaded system assets')
        this.loaded = true;
        this.pubsub = new lib.SubscriptionCore()
        this.loadSystem()
    }

    startThreads(){
        lib.threadPool.start()
        lib.threadPool.threads.start()
    }

    loadSystem(){
        ;(function(){
            this.loadDrivers();
        }.bind(this))();

        ;(function(){
            //this.startThreads()
        }.bind(this))();
    }

    loadDrivers() {
        /* download and call onLoadDrivers */
        lib.log('Load Drivers')
        Assets.load(FILES.drivers, this.onLoadDrivers.bind(this))

    }

    onLoadDrivers(){
        /*
        Load the init memory module, load the init system memory
        then startDrivers().
         */
        this.drivers = new DriverManager()
        this.drivers.mount(this)
        lib.log('Loaded driver assets, starting base drivers.')
        let memId = lib.MEMORY.id()
        this.memory = new lib.MEMORY()
        this.memory.loadInitState(this, INIT_SYSTEM_MEMORY)
        lib.log('system loaded drivers. Send ready')
        this.pubsub.emit('Drivers.ready')
    }
}

self.system = new System()

}
