/**
 * @param {Window|Element} node
 * @param {string} event
 * @param {Function} fn
 * @param {AddEventListenerOptions|boolean=} opt
 */

function addListener(node, event, fn, opt){

    node.addEventListener(event, fn, opt || (opt === false) ? opt : true);
}

/**
 * @param {Window|Element} node
 * @param {string} event
 * @param {Function} fn
 * @param {AddEventListenerOptions|boolean=} opt
 */

function removeListener(node, event, fn, opt){

    node.removeEventListener(event, fn, opt || (opt === false) ? opt : true);
}

/**
 * @param event
 * @param {boolean=} prevent
 */

function preventEvent(event, prevent){

    event.stopPropagation();
    /*prevent &&*/ event.cancelable && event.preventDefault();

    //event.stopImmediatePropagation();
    //event.returnValue = false;
}

function getByClass(root, name){

    return root.getElementsByClassName(name)[0];
}

function addClass(node, classname){

    node.classList.add(classname);
}

function removeClass(node, classname){

    node.classList.remove(classname);
}

function setStyle(node, style, value){

    value = "" + value;

    if(node["_s_" + style] !== value){

        node.style.setProperty(style, value);
        node["_s_" + style] = value;
    }
}

function setText(node, value){

    node.firstChild.nodeValue = value;
}
