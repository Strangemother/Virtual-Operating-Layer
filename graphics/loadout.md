A concept of the loadout to perform from file to view.

1. A user can implement the higher level notation without accessing the view.
  This can be a top level yaml, with component placers.
  Changes occur through stream edits or original file manipulation.
2. Lower level (pushed) provides ab actract of drawing; sent to the graphics layer as a compiiled component to call upon
3. Stream execute manipulates the view using a standard protocol


The archiecture is bi-directional, as graphics event piped from a display interface should drive the UI without lag and stream those changes back to the host. The host may act upon the given events speeding up graphical throughput and allowing such layers as GL and distant connected UI controllers.


A single UI may be connected-to by many hosts. Each accepting events and performing parallel work.

Layer types are driven through the API. They consist of HTML, GL, 3D. components are layers through the _master_ api.

+ Instansiation routines
+ base draw routines
+ communications and threads
+ Driver loading
