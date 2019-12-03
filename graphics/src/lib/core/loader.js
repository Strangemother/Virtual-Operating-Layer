/*
The loader function allows dynmic insertion to a HTML view using stndard js.
The injection required a few funadamental functions.

    loader.load('foo.js')
 */
;(function(){

    var requirements = [
    'Function',
    'Math',
    'createElement'
    ]

    var isA =  function(a,b){ return a instanceof (b || Array);}
        //-- some minifier optimisation
        , D = document
        , getElementsByTagName = 'getElementsByTagName'
        , length = 'length'
        , readyState = 'readyState'
        , onreadystatechange = 'onreadystatechange'
        //-- get the current script tag for further evaluation of it's eventual content
        , scripts = D[getElementsByTagName]("script")
        , scriptTag = scripts[scripts[length]-1]
        , _paths = {}
        , script  = scriptTag.innerHTML.replace(/^\s+|\s+$/g,'')
    ;

    var checkLoaded = scriptTag.src.match(/checkLoaded/)?1:0
        //-- keep trace of header as we will make multiple access to it
        ,header  = D[getElementsByTagName]("head")[0] || D.documentElement
        , urlParse = function(url){
            var parts={}; // u => url, i => id, f = fallback
            parts.u = url.replace(/#(=)?([^#]*)?/g,function(m,a,b){ parts[a?'f':'i'] = b; return '';});
            return parts;
        }
        , paths = function(){
            return _paths;
        }
        ,appendElmt = function(type,attrs,cb){
            var e = D.createElement(type), i;
            if( cb ){ //-- this is not intended to be used for link
                if(e[readyState]){
                    e[onreadystatechange] = function(){
                        if (e[readyState] === "loaded" || e[readyState] === "complete"){
                            e[onreadystatechange] = null;
                            cb();
                        }
                    };
                }else{
                    e.onload = cb;
                }
            }
            for( i in attrs ){ attrs[i] && (e[i]=attrs[i]); }

            e.dataset.ket = _paths[url] = (Math.random() * 100 ).toString(32);
            header.appendChild(e);
            // return e; // unused at this time so drop it
        }
        ,load = function(url,cb){
            if( this.aliases && this.aliases[url] ){
                var args = this.aliases[url].slice(0);
                isA(args) || (args=[args]);
                cb && args.push(cb);
                return this.load.apply(this,args);
            }
            if( isA(url) ){ // parallelized request
                for( var l=url[length]; l--;){
                    this.load(url[l]);
                }
                cb && url.push(cb); // relaunch the dependancie queue
                return this.load.apply(this,url);
            }
            if( url.match(/\.css\b/) ){
                return this.loadcss(url,cb);
            }
            return this.loadjs(url,cb);
        }
        ,loaded = {}  // will handle already loaded urls
        ,loader  = {
            aliases:{}
            ,loadjs: function(url,cb){
                var parts = urlParse(url);
                url = parts.u;
                if( loaded[url] === true ){ // already loaded exec cb if any
                    cb && cb();
                    return this;
                }else if( loaded[url]!== undefined ){ // already asked for loading we append callback if any else return
                    if( cb ){
                        loaded[url] = (function(ocb,cb){ return function(){ ocb && ocb(); cb && cb(); }; })(loaded[url],cb);
                    }
                    return this;
                }
                // first time we ask this script
                loaded[url] = (function(cb){ return function(){loaded[url]=true; cb && cb();};})(cb);
                cb = function(){ loaded[url](); };
                appendElmt('script',{type:'text/javascript',src:url,id:parts.i,onerror:function(error){
                    if( parts.f ){
                        var c = error.currentTarget;
                        c.parentNode.removeChild(c);
                        appendElmt('script',{type:'text/javascript',src:parts.f,id:parts.i},cb);
                    }
                }},cb);
                return this;
            }
            ,loadcss: function(url,cb){
                var parts = urlParse(url);
                url = parts.u;
                loaded[url] || appendElmt('link',{type:'text/css',rel:'stylesheet',href:url,id:parts.i});
                loaded[url] = true;
                cb && cb();
                return this;
            }
            ,load: function(){
                var argv=arguments,argc = argv[length];
                if( argc === 1 && isA(argv[0],Function) ){
                    argv[0]();
                    return this;
                }
                load.call(this,argv[0], argc <= 1 ? undefined : function(){ loader.load.apply(loader,[].slice.call(argv,1));} );
                return this;
            }
            ,addAliases:function(aliases){
                for(var i in aliases ){
                    this.aliases[i]= isA(aliases[i]) ? aliases[i].slice(0) : aliases[i];
                }
                return this;
            }
        }
    ;
    if( checkLoaded ){
        var i,l,links,url;
        for(i=0,l=scripts[length];i<l;i++){
            (url = scripts[i].getAttribute('src')) && (loaded[url.replace(/#.*$/,'')] = true);
        }
        links = D[getElementsByTagName]('link');
        for(i=0,l=links[length];i<l;i++){
            (links[i].rel==='stylesheet' || links[i].type==='text/css') && (loaded[links[i].getAttribute('href').replace(/#.*$/,'')]=true);
        }
    }

    // eval script tag content if needed
    scriptTag.src && script && appendElmt('script', {innerHTML: script});


    this.global(loader, requirements, 'loader')
}).apply(Header)
