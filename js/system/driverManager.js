/*
Maintain a list of drivers for user feedback.
Start stop and API control.
 */

class DriverManager extends Driver {

    init(){

    }

    mount(sys){
        sys.pubsub.add('MEMORY.init', this.memoryInit.bind(this))
        sys.pubsub.add('Drivers.ready', this.driversReady.bind(this))
    }

    memoryInit(MEM_DATA){
        this.loadPersistentDrivers(MEM_DATA)

    }

    loadPersistentDrivers(MEM_DATA){
        lib.log('DriverManager heard memoryInit')
        /* Load data for the drivers. Initial driver paths and states*/
        let drivers = MEM_DATA.drivers;
        Assets.load(drivers, function(){
            this.onLoadPersistentDrivers(MEM_DATA)
        }.bind(this))
    }

    list(){
        return Object.keys(DRIVER_MOUNT)
    }

    onLoadPersistentDrivers(MEM_DATA){
        /* The required drivers are loaded and ready for boot.
        The initial data for each driver should be ready. */
        let driverIDs = MEM_DATA.ids
        for(let id in driverIDs) {
            let uuid = driverIDs[id]
            if(DRIVER_MOUNT[uuid] == undefined) {
                lib.log('!! Missing driver', uuid)
                console.warn(`Cannot locate driver mounted as "${uuid}". Ensure it is Asset loaded`)
                continue
            }

            lib.log('loading', uuid);

            for(let pos in DRIVER_MOUNT[uuid]) {
                let driverClass = DRIVER_MOUNT[uuid][pos]
                let data = MEM_DATA[uuid];
                MEM_DATA.loadedDrivers.push([uuid, data, driverClass])
                lib.log('Class', uuid, driverClass.name)
            }
        }
    }

    loadMountList(nameList, callback) {
        /* given a list, install each string name as a driver.
        The driver should exist. */
        lib.log('loadMountList')
        let r = {}

        for (var i = 0; i < nameList.length; i++) {
            let uuid = nameList[i];
                let driverClass = lib[uuid]
                this.installDriver(driverClass)
                // let data = system.memory.get(uuid)
                // //let data = MEM_DATA[uuid];
                // //MEM_DATA.loadedDrivers.push([uuid, data, driverClass])
                // system.memory.get('loadedDrivers').push([uuid, data, driverClass])
                // lib.log('Load Driver:', uuid, driverClass.name)


            r[uuid] = lib[uuid]
        }

        if(callback) {
            callback(r)
        }

        return r
    }

    installDriver(_Driver) {
        /* install a driver as if loaded through the loading system.
        The driver can hook without this function, however some events may
        be missed.

        The display sytem can attach:

            s=new DisplayScreen
            s.mount(system)

        but will miss memory data unless attached through 'onloadedPersistDrivers'.
        Therefore this function call installation correctly:
         */

        // Push the mounting of the driver through the mount point.
        lib.driverMount(_Driver, false);
        let uuid = _Driver.id()
        if(DRIVER_MOUNT[uuid] == undefined) {
            lib.log('!! Installing driver did not mount', uuid)
            return
        };

        let data = system.memory.get(uuid)
        system.memory.get('loadedDrivers').push([uuid, data, _Driver])
        lib.log('Class', uuid, _Driver.name)
        let driver = new _Driver(data)
        lib.log('start', uuid)
        SYSTEM_DRIVERS[uuid] = driver
        driver.mount(system)

        return driver;
    }

    driversReady(){
        lib.log('driverManager driversReady, startDrivers')
        this.startDrivers()
    }

    startDrivers(){
        /* Read the memory initDriverData(), for each set of
        [unique_name, init_data, class]  - boot the class
        and mount the driver into SYSTEM_DRIVERS. */
        lib.log('Driver data ready. startDrivers')
        for(let driverSet of system.memory.initDriverData()) {
            let [name, data, klass] = driverSet;

            // Boot driver
            let driver = new klass(data);
            lib.log('start', name);
            SYSTEM_DRIVERS[name] = driver;
            driver.mount(system)
        }
    }

    unmountDriver(name){
        SYSTEM_DRIVERS[name].detach();
        SYSTEM_DRIVERS[name].close();
        delete SYSTEM_DRIVERS[name];
    }

}


lib.driverMount(DriverManager)
