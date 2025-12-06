
const customPointer = function(show=true){

    let p = new VisiblePointer()
    p.enable()
    return p
}

class VisiblePointer extends Eventor {

    static atPosition(e) {
        /* a static method (`this` is window), to generate a new point at the
        pointer event position.*/
        let p = customPointer()
        p.locked = false
        // const mouseY = e.clientY
        // const mouseX = e.clientX
        p.cloneLockPosition(e)
        return p
    }

    get cloneNode() {
        return true
    }

    setup(selector='.pointer'){
        let unit= document.querySelector(selector)
        this.entity = this.cloneNode? unit.cloneNode(true): unit;
        document.body.appendChild(this.entity)
    }

    cloneLockPosition(e) {
        this.clonePosition(e)
        this.locked = true
    }

    mousemove(e) {
        if(this.locked) { return }
        this.clonePosition(e)
    }

    mousedown(e){
        // console.log('mousedown')
        this.entity.classList.add('mousedown')
        if(this.locked) { return }
        this.clonePosition(e)
    }

    mouseup(e){
        // console.log('mouseup')
        this.entity.classList.remove('mousedown')
        if(this.locked) { return }
        this.clonePosition(e)
    }

    contextmenu(e) {
        /* The builtin _right click_ menu is not applied.
        Instead we have pointer contexts' and their layers.*/
        e.preventDefault();

        this.contextPointer = VisiblePointer.atPosition(e)
    }

    clonePosition(e) {
        const mouseY = e.clientY;
        const mouseX = e.clientX;
        // cursorRounded.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0)`;
        this.entity.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0)`;
    }

    enable(show=true) {

        document.body.classList[['remove', 'add'][+show]]('hide-mouse')
        super.enable(show)
        bus.on('handle-event', this.handleEvent.bind(this))
    }

    handleEvent(e) {
        let t = e.target
        let direction = e.styleName || t.dataset.direction
        // console.log('handle-event',e.type, direction)

        let show = {'mouseout': false, 'mouseover': true}[e.type] // out false / in True
        this.entity.classList[['remove', 'add'][+show]](direction)
        if(e.unlock != undefined) {
            this.locked = !e.unlock
        }

        if(this.locked) { return }

        this.entity.querySelector('.visible').style.padding=""

        if(e.action) {
            this[e.action](e)
        }
    }

    copyPlacement(e){
        /*
        Copy the style location of the given entity.
         */
        // width, height, top, left.
        this.setPosition(e.target.getBoundingClientRect())
        this.mouseoutUnlock = true
    }

    setPosition(d) {
        /*
        bottom: 883
        height: 64
        left: 761
        right: 825
        top: 819
        width: 64
        x: 761
        y: 819
        */
        console.log('setPosition')
        this.entity.style.transform = `translate3d(${d.x+d.width*.5}px, ${d.y+d.height*.5}px, 0)`;
        this.locked = true
        this.entity.querySelector('.visible').style.padding=`${d.width*.5}px ${d.height*.5}px`
    }
}
