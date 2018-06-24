/* Memory module keep data throughout the application, allowing the
allocation of permanent storage across the FS for speed and best throughput.

Key lay points for memory are:

RAM - Not accessed through the UI, however VOL options can alter RAM allocation
VOL - data storage through a service or VOL -
LS - Localstorage within the CFI or browser
IPFS - Global peering through a socketed data layer.
*/
{

let MEM_DATA = {
    drivers: []
    , loadedDrivers: []
}

class MEMORY extends lib.Driver {

    static id(){
        return `base.memory`
    }

    init(){
        lib.log('load memory')
    }

    initDriverData(){
        return MEM_DATA.loadedDrivers
    }

    get(key, _default) {
        let d = MEM_DATA[key];
        if(d == undefined) {
            return _default;
        };
        return d;
    }

    put(key, data) {
        MEM_DATA[key] = data;
        return true;
    }

    loadInitState(sys, initData){
        /* Open the memory and prepare for read.
        The memory should reinit to the previous storeed state If any init persistent data
        exists (such as soft state close and memory hibinate) */
        lib.log('load init memory data')
        Object.assign(MEM_DATA, initData)
        sys.pubsub.emit('MEMORY.init', MEM_DATA)
    }
}

class MemoryDriver {
    constructor(id, _class){
        this.id = id;
        this._class = _class;
    }
}

lib.driverMount(MEMORY)
}
