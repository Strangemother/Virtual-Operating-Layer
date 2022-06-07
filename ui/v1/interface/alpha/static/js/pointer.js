
const customPointer = function(show=true){

    let p = new VisiblePointer()
    p.enable()
    return p
}

class VisiblePointer extends Eventor {


    mousemove(e) {
        this.clonePosition(e)
    }

    mousedown(e){
        // console.log('mousedown')
        this.entity.classList.add('mousedown')
        this.clonePosition(e)
    }

    mouseup(e){
        // console.log('mouseup')
        this.entity.classList.remove('mousedown')
        this.clonePosition(e)
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
        let direction = t.dataset.direction
        // console.log('handle-event',e.type, direction)
        let show = {'mouseout': false, 'mouseover': true}[e.type] // out false / in True
        this.entity.classList[['remove', 'add'][+show]](direction)
    }
}
