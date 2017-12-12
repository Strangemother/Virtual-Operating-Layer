{
class Dev {

    start(){
        this.delay = 2000
        this._globals = undefined
        this._window = Object.keys(self)
        this.gCheckTimer = window.setInterval(function(){
            this.checkGlobals()
        }.bind(this), this.delay)
    }

    stop(){
        window.clearInterval(this.gCheckTimer)
    }

    checkGlobals(){
        if(this._globals == undefined) {
            this._globals = lib.globals(this._window)
        }

        let globals = lib.globals()
        let change = globals.length - this._globals.length
        if(change == 0) { return }

        if(change > 0) {
            console.warn('New Globals', globals);
            this._globals = globals;
            let minutes = 5;
            if(this.delay > 1000 * minutes * 60) {
                return
            };

            this.delay += 1000;
        } else {
            console.log('Removed Globals!', globals)
        }

    }
}

self.dev = new Dev();
dev.start()
}
