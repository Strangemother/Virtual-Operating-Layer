/* A system driver.

A System driver integrates into the lib and the system automatically.
The unique "id()" provides a name import for usage. The system will call
to memory for a driver initiation. 
 */

class Driver {
    /* a base drvier handles mounting into the management layers.
    Data mayhe initialized vis an init object.
    */
    constructor(data) {
        this.data = data || {}
        this.init()
    }

    static id(){
        /* return a unique ID for this driver, used for
        memory mapping*/
        return this.name
    }

    id(){
        return this.constructor.id()
    }

    init(){
        /* The drvier is initialized. All the required settings are ready
        for use. The driver is not mounted.*/
        lib.log(`init ${this.id()}`)
    }

    mount(system){
        /* Called by the system when driver initialization is complete and
        mounting onto the system should start. Integration with pubsub
        and threads before announce */
        lib.log(`Mounted ${this.id()}`)
    }

    announce(){
        /* A mounted driver has finished initializtion and mount process.
        The ready drvier is integrated into the system and ready to perform
        it's natural action.
        Announce the driver for application mounted by the next layer.
        Expect incoming.*/
    }

    detach(){
        /* Soft remove the action of the driver. Inert in effect, the driver
        should run in an inactive state - for alternaive similar driver
        connections or such...*/
    }

    close(){
        /* Cleanly and safely shutdown the driver.*/
    }

    destroy(){
        /* Perform any action to complete remove the driver from the system
        or functionality. unlike 'close' of which expects a future 'init',
        the destroy should remove all entry of the driver. */
    }

}

class ExposedDriver extends Driver {
    /* Act like a driver, with auto mounting for drivers
    acting alone. */

    static wakeIdentity(){
        /* An exposed driver automatically mounts through 
        the ID. */
        return `wake.${this.id()}`
    }


    static wake(name){
        /* Preliminary start method. Used to inboke pre conditions before hook.*/
    }

    hook(name, data){
        /* capture the GUI the data is the wake event information.
        Stated by the wake name. */
        console.log(`${this.id()} hook`, name)
    }
}

DRIVER_MOUNT = {}

let driverMount = function(driver, libMount=true){
    /* Provide mounting for a driver */

    let md = {}
    md[driver.name] = driver;

    if(libMount == true){
        lib.mount(md)
    }

    let _id = driver.id()

    if(_id != undefined) {
        if(DRIVER_MOUNT[_id] == undefined) {
            DRIVER_MOUNT[_id] = []
        }

        //lib.log(`.. Accepted driver ${_id}`)
        DRIVER_MOUNT[_id].push(driver)
    }

}

lib.mount({ Driver })
lib.mountFunction(driverMount)
