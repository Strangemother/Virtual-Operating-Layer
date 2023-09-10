# Interface

The primary interface is not "windows" or _tiles_ of pixel data and text. Indeed those elements are utilised but I don't want to simply clone the existing ideas. Some concepts are solid:

+ The interface is independant of the root runtime, acting within a context and layer
+ The graph engine needs a root interface (stdout)

_conceptual:_ When a user _clicks_ a graph pointer, a new _window_ spawns relative to the pointer context. All elements have their unique display requirements. Some of these are classical _blocks of text_. However given the CGA root of the runtime, this should be geometrically presented

+ orbs
+ paths
+ table grids matrix presents



https://en.wikipedia.org/wiki/Attentive_user_interface
https://en.wikipedia.org/wiki/Natural_user_interface
https://en.wikipedia.org/wiki/Zooming_user_interface
http://www.oxygen.lcs.mit.edu/
https://en.wikipedia.org/wiki/Literate_programming
https://en.wikipedia.org/wiki/Calm_technology
https://en.wikipedia.org/wiki/Category:User_interface_techniques
https://en.wikipedia.org/wiki/Ambient_intelligence
https://en.wikipedia.org/wiki/User_interface_plasticity
https://en.wikipedia.org/wiki/Context_awareness
https://help.tableau.com/current/blueprint/en-us/bp_why_visual_analytics.htm


# Concept

The arch for the new philosophy starts with a fundamental question, "What is an app?" - an to redefine, what is the _idea_ people currently hold of an "application". This has a range of answers owing to the myriad of terms applied to a single _application_. Is CS it's a _program_ to perform input and output on a system, yield changes and usually presenting information to a user, in the form of text and graphics.

An app may manifest as a 'program' or sub-program within an eco-system, such as windows apps, ios/apple apps, or even the more core "BIOS" may be considered an app in its own right. Thus an app has two purposes; perform interactive changes within a system, and optionally present that information to a user.

Semantically I feel a 'application' or 'program' are the same here. The term is interchangable for both. A "programme" defines a sequence of [printed] steps for an output - probably coming from the latin _written information_ (citation needed). The term 'application' defines action of putting something into operation, or a define request of actions (A paper of commands) for a host to action.

Simplifiying this as two rules:

+ Performs system changes to perform an action
+ Presents a state to the user

A user may interact with an application. Thus it needs a scope of interactivity; visual (text), audio ... etc.

Extended Rules:

+ Interactivity for input/output
+ isolated from the wider system, existing upon and within - but not apart of - the main system
+ The result is usually a product of function

With this we can define "what is an app". As it has actions to change the state of the (primary application internal) machine and present those changes to give us (the human) a useful result.


## Consider the Cup.

With the definition, many _things_ may be defined as an "app". A Cup is an app. A kettle is a better example of a wholesome app. A toothbrush is an app; an electric toothbrush is a better app.

Therefore the "application" and "program[me]" are helpful bags of _functions_ to mitigate a problem, or assist with the process of a current task. The cup is a fantastic application of holding liquid in a stable position, such that we may siphon small amounts at regular intervals ... _easily_.

Fundamentally we don't need _the cup_. Life would exist without it; albeit less efficiently. We could use bowls, plates, or even a beautiful vase. We could invent a method to generate a spoonful of coffee or tea for every sip. But functionally none of these methods are better than the century old design of a deep small bowl, with a handle for a few fingers.

The cup can be altered and updated - riding the wave of micro iterations to bring us unbreakable, common sized, colourful versions of the same thing. However you step back **thousands** of years, and a 10th century farmer will recognise your cup.

----

Question is - who the hell cares about cups? And why is this related to software apps.

Although abstract I feel a cup and a linux app are within the same group of human things. Both _perform a task to ensure I can do another task easier_. We compound this to flow complex webs of dependencies. In software we live upon a mature codebase of like 70 years, and knowledge built 100 years ago. With physical objects My cup exists on a table, in a room, within a house... All disected into useful areas of functionality for my existence.

> So when considering an "app", is it a spanner? or a 2D grid of text and graphics.

An application in the current software world is built within the target eco-system, leveraging code components given through a common-api. They all look the same; because familiarity is important to ensure user adoption - humans don't want a task to be harder. In every case we (humans) constantly adapt something to make it better.

With software we've built upon the desktop terminology; as for hundreds of years - and through the transition of a paper-based world to digital - we understood _documents_ and _files_. This does go deeper with memory formats (registers) based upon ye old jacquard looms.

We have 'pens' that don't write, or 'documents' that don't exist. Perhaps "speakers" that don't really actually voice their opinon. Or my favourite Uppercase letters, that no longer live within a "case" upon the upper shelf of my printing press.

So when considering an "app", is it a spanner, wooden printer, or a 2D grid of text and graphics. Should we assume _An application is a window of text and pictures_, or can it be something more? If we had the ability to integrate _the cup_ into our _programme_, it would be a function of our _soft_-wares, and thus break the concept of an app today.


## Alter

underneath a visual interface (and any user applications) is a synthetic graphing and context layer, producing a runtime as required. Unlike classical computing, the goal for VOL is true distribution and to step-away from the von-neuman archiecture.

The "application" doesn't exist in a manner fitting to todays classical style. Currently the general ethos is _STORE_, _LOAD_, _EXECUTE_ with an application ferring information between integrated components. The app is considered a middleman to action.


Currently the flow to using an app:

1. A developer defines a procedure within an app
2. The app is distributed to the users machine
3. The user loads the app into a execution state
4. The system executes the procedures ...
5. Calling upon local resources until done

The disection of roles is clear and well defined. A developer defines procedures, a system hosts the procedures until a user executes on command. This is fundamental to Von-Neuman computing.

---

In a VOL this doesn't change. The system will still maintain a range of actions to process, and the user may still _action_ upon customised procedures. But the processing of routines acts outside the micro-runtime a developer usually maintains for a task.

in a graph layer, the 'app' will drive many pointers across a graph of smaller procedures or pointer motion. This actions the required steps for the task. Each point in the graph yields changes to the _environment_ of the existing space. It exists within a microcosm of graph parts, built by the host and _given_ to the "app" when executed.

The input of the system won't fit a linux style piping input. It's a tape of pointer movements, and any additional pointer motions.

The interface output is not a 2D panel of text yielding the current state, it's a solution existing on the graph, of which must be reduced with a reading utility. This should attach the target pointers and present the content by emiting results through the cell membrane, into sibling machines.

---

To synopsis the above, An app is a distinct set of procedures, called upon by a user. The 'app' interact with a system to yield a result. We see that a 2d panel of information may not be the first choice for interfaces.

In thought it seems an application could be a heterogeneous collection of tools, connected beneath the primary interface, aligning many discrete views for one result. For example a simple _script_ of sorts, is an execution  and _potentially_ a text log. However the script may opt to present non-textual information, such as an image.

Indeed many things are _squares_, such as a video panel. But why must a content-panel be _square_.
As interfaces have evolved, computing science has concatenated newer ideas upon existing paradigms. Considering how we _click_ or _push_ a "button" - it's a mechanical actuation. But we now have hovers and intent, we manifest strength or even fingerprints to a UI.

Therefore the experience we once had - mechnical buttons, things that _clicked_ - were born from a pre-information age. They exist within the physical and our lexicon has molded the meaning to something relevent. This isn't a negative for we humans normalise everything. For example, in the victorian era  the word "soon" meant _now_ as in _I'll be there immediately._. However (I assume) everyone was late, and now _soon_ means _some-time in the very near future_.

But with this we attain a ill-fitting nomenclature, or apply functionality (or intend) to a _thing_ without considering its _own_ philiosphy. We start to forget the identity of the rebranded thing and hold onto what it means - tugging the misrepesented brand with it.

A wider example is an article of text; or closer _a website_ (such as a news page). We ask ourselves _is the document style presenting "an article", the best method?_. Focusing on HTML as it acts as a pseudo philisphoy for presenting information. In the modern standard we have literal semantics to identify parts of a written stream of text.

As a high level these include 'headers' `h1 ... h6` and `<article>`, `<section>` and a few hundred more. We also include the fundamental `p` for a _paragraph_, with _spans_, and _em_ for emphasis. Indeed with was excellent for the paper printed form -why?

+ cheap
+ predicable
+ reliable

To think, if _wax on crushed charcoal printing_ was somehow the adopted best practice for spooling prints 400 years ago, would we still have structured headers, predicable alignments, or even a _document_ with a header/footer? It could all have started with white wax on charcoal paper and an article would be fresh every paper.  The chosen medium would be destroyed for heat after a single sitting; the _font_ may not be "times new roman" - but rather "Perma Wax Stamp Normal". We wouldn't have predicable headers, we've have _larger wax stamp_ or _smaller_...

---

Stepping through _the alterntive universe_ is a great mind-game to expand what is optional or fundamental for us humans. Here we see the interface of things we see today are an adoption of existing ideas; smashed into something we concure is useful.

In more recent design philosphies we are begginging to understand cognitive overload, and information disection. It's no longer the best method to give _Everything to the user_, but rather walk sincere processes until the user attention is released. In the last 20 years UX/UI has adopted a mindset of _user first_, and manageable informationable flows.

We now understand a _text article_ is more than a page (of paper) filled with paragraphs and commas. With links, and _other pages_, and sub-information, Todays _article_ is a media rich digestion of 2d or even 3d data. Where the user walks many congitive micro-paths, for a wholesome view of a resource.


---

Personally I feel a _3D_  computing world is long overdue. I was inspired by Jonny Mnemonic as a child and couldn't wait to step into a virtual world and battle with cyber criminals. I still remember the disapointment to this day, when I learnt -that's not what the internet is. Fast-forward to 30 years later and the _desktop_ (and internet) have barely evolved from a _start!_ button.

I feel this isn't the fault of people - standard daily drivers of computers. As it's not their job to accomodate a new ideology. "People" (being a non-descript daily end-user) is now a ubiquotious _everyone_ from the ages 6 to 100. It's a tall order to expect all users to adopt a brand new methods of _computing_. As such the _start_ button, or anything standardised - has suck. And will always stick until something better is made.

---

It's due to this virtual 3D environments have not been mass adopted. It's all just too crap - and also owned by massive conglomerates. When 3D, I'm met with a pointer and pancake view, or need to signin - or peering through tubes to a pseudo reality. Sure once immersed, it does feel like I'm battling futuristic robots - But if the onboarding to an experience is prohibavly tedious - _people_ (me) will likely get bored and learn to _adapt_ or move on.

So can an operating system be _inheritnly_ 3D? At the moment I feel no. As no one wants to faff around with 3D spinning cubes of pancakes or seeing cupuscular rays due to a loading sound card. It all means nothing.

Stepping outside that idea; perhaps presenting _things_ (functions) and _result work_ as 3D objects could be a method forward. However larger questions arise such as - what about actual flat content, such as a text document? Again no-one wants to handle orbs of text or cubes of hard-drives, However utilising more than just a 2D planar for presenting data may be advantagous.
