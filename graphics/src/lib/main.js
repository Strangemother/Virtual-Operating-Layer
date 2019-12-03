class Noder {
    /*
    The very base extended by the machinery to be the parent of everything.
     */
    create(){

    }

    createFragment() {
        return this.parent.createDocumentFragment();
    }
}

class Machine extends Noder {
    /* The high level implement base for computing callbacks. All side-cart loaded
    functionality is accessed throug the machine. */

    load(filename) {
        /* Live load functionality to request back-end files using the core loader
        */
        return loader.load(filename)
    }
}

class View extends Noder {
    /*
    High level view management and interface layer for working with bound presenations
     */

    constructor(parent) {
        super()
        this.views = [];
        this.parent = parent;
        this.frame = this.createFragment()
    }

    documentDestroy(){
        //var newStringDoc = new Document()

        var c = this.parent.createDocumentFragment();
        var e = this.parent.createElement("body");
        e.className = "test-div";
        e.textContent = 'No content.'
        c.appendChild(e);
        //newStringDoc.appendChild(c);
        this.parent.body.replaceWith(c)
    }


    add(viewable) {
        console.log('Add to view', viewable)
        this.views.push(viewable)
    }

    start(){
        // Initiate the view construct, hooking to the internal parent and
        // writing a parnet frame.
        console.log('View start', this.frame)
        var divFrame = this.parent.createElement('div');
        divFrame.textContent = 'apples'
        divFrame.append(this.frame)
        this.view = divFrame
        this.parent.body.append(this.view)
    }

    render(node) {
        /* Apply a viewable to the draw layer. */
        console.log('View render - add item:', node)
        this.frame.appendChild(node)
        console.log(this.frame)
    }

    showFrame(element) {

    }
}

class Viewable extends Noder {
    /* A abstraction to apply UI rendering amchinery to a noder. consider
    this an abstraction of the noder and not the best element as a base.
    */
    prepare() {
        // ready the view component in a memory state for render
        this.fragment = this.createFragment()
    }
}


class PresentLayer extends Viewable {
    /* Drawing functions and event actions dedicated to drawing. Consider
    this the base layer for any drawable unit as it encompasses a unique comms
    attachment, machine connection and other 'live' attributes to work a UI.*/
}


class Perspective extends PresentLayer {
    /* A Persoective defines a single drawable unit loaded into memory for
    persistent view management. A system may have may perspectives, each performing
    their own drawing through unique coms and phyical draw layers.
    */
}


class TextPerspective extends Perspective {
    /*  A Linear text presentation perspective, providing a core for standard text
        rendering.
     */
    constructor(parent) {
        super()
        this.parent = parent;
    }
}


class StandardOutputPerspective extends TextPerspective {
    // a stdout linear text writer.
    // redirect stdout.
    stdout(a){
        console.log.apply(console, arguments)
        this.addText(a)
    }

    addText(a){
        let texts = []
        if(Array.isArray(a))  {
            for (var i = 0; i < a.length; i++) {
                texts.push(this.textualElement('span', a[i], 'stdout-argument'))
            }
        } else {
            texts.push(a)
        }

        let e = this.textualElement('li', texts.join(' '))
        this.addElement(e)
    }

    addElement(htmlElement) {
        console.log('StandardOutputPerspective addElement')
        this.fragment.append(htmlElement)
    }

    textualElement(elementType, textContent, className) {
        var e = this.parent.createElement(elementType);
        e.className = className || "stdout-line";
        e.textContent = textContent
        return e
    }

    render(view) {
        // Render (first time) This element to the given view

        var divFrame = this.parent.createElement('div');
        divFrame.appendChild(this.fragment)
        this.frame = divFrame
        view.render(divFrame)
        //this.frame.appendChild(e)
    }
}

// var c = document.createDocumentFragment();
// for (var i=0; i<10000; i++) {
//     var e = document.createElement("div");
//     e.className = "test-div";
//     c.appendChild(e);
// }

// document.body.appendChild(c);
// loader.load('foo.js')

class Start extends Noder {
    /* An executor function to start a view */

    start(parentDocument){
        console.log('Start')
        let machine = new Machine()
        let view = new View(parentDocument)
        head.global(machine, [], 'machine')
        head.global(view, [], 'view')
        view.start()
    }

    run(parentDocument){
        this.start(parentDocument)
        this.basePerspective(parentDocument)
    }

    basePerspective(parentDocument){
        /* Draw the initial stdout text perspective.*/
        let stdoutRedirect = new StandardOutputPerspective(parentDocument)
        view.documentDestroy()
        view.add(stdoutRedirect)
        head.global(stdoutRedirect.stdout.bind(stdoutRedirect), [], 'stdout')
        stdoutRedirect.prepare()
        stdoutRedirect.render(view)
    }
}


;boot = new Start();
boot.run(document);

// machine.load('foo.js')
stdout('Hello World')
stdout('Another sentence.')

/*

    Machine: spawn unit for system work; processes - coms etc.

    View: a component layer for visual abstraction
    layer: A component applied to a view to contain display material
    perspective: A presentation layer for all extends, applying the view
                 to machines and screens.

    TextLayer: presents linear text
    DrawLayer: A canvas drawing layer

 */


// loader.load('foo.js')
