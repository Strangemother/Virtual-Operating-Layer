/*
The VOL - Virtual Operating Layer defines the computational layer supporting
the interface API and UI.

In context the VOL is the backend (python) connected through the VOL container.
If the BIOS (and ico) is _remote_ or loaded off a VOL Container, this file
acts as a psuedo responder for the offline service.

Some external attributes exist for VOL hooking - and container overloading.
 */
{

class VOLContainer {
    constructor(){
        this._booted = false
        this.haltExecute = false;
        this.windowKeys = Object.keys(self)
        this.attach()
        this.setImmediate()
    }

    attach(){
        console.log('VOLContainer')
        let id = Math.random().toString(32)
        addEventListener(id, function(e){
            // removeEventListener(id)
            let callback = e.detail.callback
            callback(this)
        }.bind(this))

        dispatchEvent(new CustomEvent('VOL', {
                detail: {
                    id: id
                }
            })
        )

        // wait for response.

        // Expect the BOOT event.. Respond with execute.
        addEventListener('BOOT', function(e){
            if(this._booted) {
                console.error('Two BOOT commands?')
                return false
            };

            console.log('VOL BOOT')
            this._booted = true
            dispatchEvent(new CustomEvent('EXECUTE'))
        }.bind(this));
    }

    setImmediate(){
        let standardResponse = function(e, d){
            d = d == undefined ? {}: d;

            setTimeout(function(){
                let id = e.detail.id;
                console.log('Simulate network timeout', id)
                dispatchEvent(new CustomEvent('IMMEDIATE_RESPONSE', {
                    detail: Object.assign({ id: id}, {data: d})
                }))
            }, 1)
        };

        /* Capture and alter the execution of the ICO.*/
        addEventListener('EXE_BIOS', function(e){
            let d = {
                data: {
                    // SELECTED: 'CAE'
                }
            };

            standardResponse(e, d)
        })

        /* Handle the SYS execution of head.*/
        addEventListener('HEAD', function(e){
            let d = {
                // HEAD: 'js/goo.js'
            };

            standardResponse(e, d)
        })

        addEventListener('ASSETS', function(e){
            let d = {
                // loadset: 'cake'
            };

            standardResponse(e, d)
        })

        addEventListener('INIT', function(e){

            let d = {
                // loadset: 'initial'
                // , funcName: 'initializeSystem'
                // , assets: SYS.ASSETS
            };

            standardResponse(e, d)

            let keys = Object.keys(self)
            var oKeys = this.windowKeys
            let dd = keys.filter(function(i){
                return oKeys.indexOf(i) == -1
            }.bind(this));

            console.log('init', dd)
        }.bind(this))


        addEventListener('OFFLOAD', function(e){
            console.log('OFFLOAD')
            standardResponse(e)
        })
    }
}


(function(){

    let container = new VOLContainer()
})();

}
