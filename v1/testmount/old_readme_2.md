# Assets

Load core assets for the desktop framework

# Features

+ Multi screen though websockets and protobuff
+ Abstract Syntax Tree

    Analyse/rewrite/porting of the core application through a built-in abstract
    reader

+ Auto docs.
+ Multithreading to the core.
    + fully Off-thread for main features
    + multi-core through server connection and additional threads
+ Class tree renderer
+ ASM
+ Class baking
+ Persistent data through graph database

# Noted Appliance

+ full CEF app

The full application of the core desktop extends into the CEF container. Producing
a complete platform with native integration.

The "VOL" (Virtual Operating Layer) is a GUI for rendering an app, designed [above]
with iso-morphic extensions for bridging core code into UI code.

With python, JS and a lot of clever the container (python local) serves a CEF
with an app driving the full implementation (JS, HTML). Applying bi-directional
application programming and layering all the concepts wanted.

+ (VOL) Python backend
+ (CEF) Middle tier
+ ES6 frontend
+ (GFS) filestorage
+ (Hyperdex, PROJECTNAME) Hyperspace distributed data layer
+ (Code) Cloud connection

# Purpose

A well-presented full UI layer to the scatter nux project. It will implement
all features for distributed application development, with a UI layer for
integrated environments and extended graphical development.

A UI deployable on any interface:

    + VOL CEF container for desktop localisation
    + Browser based
    + API UI Integration base (like screen VNC)
    + Mobile through remote coms


## Funz.

The core feature-set implements all the researched components for the Nux project.
Providing an open-source architecture for desktop-like applications on
a homogeneous platform.


# Structure

+ ES6
+ Assets

The interface has no layer of rendering owning rto its distributed nature. An interface is a feed of UI components fed through rendering pipelines from a GL interface, websocket instructions or another thread.
