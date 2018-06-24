/*
Base layer for importing files.
Vendors are seperated from the application.
The application will load subsets as required; first 'initial', of which
autoamtically pulls the vendors.
 */

var FILES = {

   /* libraries for the build phase - for dev and extraction tools.
   Should be removed before deploy. */
   build: [
      '/js/lib/dev/dev.js'
   ]

   , vendors: [
      '/js/vendor/IT.js'
      //, '/js/vendor/vue.min.js'
      //, '/js/vendor/jquery-3.1.1.min.js'
   ]

   /* Core features, required by all assets and closures.
   Defined elements of core load-out. */
   , lib: [
      '/js/lib/lib.js'
      , '/js/lib/errors.js'
      , '/js/lib/threads.js'
   ]

   /* First call procedure called by the boot loader. */
   , initial: [
      'build'
      , 'vendors'
      , 'lib'
      , '/js/lib/boot.js'
   ]

   /* An initial loader for a bare thread.*/
   , initializeThread: [
      'build'
      , 'vendors'
      , 'lib'
      , 'system'
      , 'drivers'
      , '/js/lib/threadHead.js'
   ]

   , parser: [
      '/node_modules/acorn/dist/acorn.js'
      , '/node_modules/acorn/dist/acorn_loose.js'
      , '/js/lib/parser/code-parser.js'
   ]

   , boot: [
      '/js/system/boot.js'
   ]

   , system: [
      '/js/system/driver.js'
      , '/js/system/pubsub.js'
   ]

   , drivers: [
      '/js/drivers/memory.js'
      , '/js/system/driverManager.js'
      , '/js/drivers/keyboard.js'
      , '/js/drivers/display.js'
   ]

   , sound: [
      '/js/drivers/beep.js'
   ]

   , display: [
      '/js/display/screen.js'
      , '/js/display/canvas.js'
      , '/js/display/canvasLayer.js'
      , '/js/display/interfaceLayer.js'
   ]


   , interface: [
      'canvas'
      , '/js/runtime/interface.js'
   ]

   , canvas: [
      '/js/canvas/text.js'
   ]
}

Assets.add(FILES)
