# Building an Operating System That Shouldn't Work: A Technical Journey

**Or: How I Spent a Decade Deleting Everything I Knew About Computing**

---

![XKCD Tech Support](https://imgs.xkcd.com/comics/tech_support_cheat_sheet.png)
*Credit: [XKCD #627](https://xkcd.com/627/) - Because sometimes the best way to understand technology is to explain it to someone who knows nothing about it.*

---

## Introduction: The Boat That Used to Be a Car

I'm going to be honest with you: I've spent the last 10 years building something that probably shouldn't exist. Not because it's impossible—I think it actually works—but because it requires deleting almost everything we know about operating systems and starting from scratch.

The Virtual Operating Layer (VOL) is my attempt to reimagine computing from first principles. It throws away Von Neumann architecture. It replaces linear code execution with graph-based, self-executing nodes. It uses topology for security instead of permission systems. And it's built on mathematical frameworks that most developers have never heard of, like conformal geometric algebra.

The key driver? Speed. And potentially a more natural way for humans to interact with machines.

But here's the problem: the concepts and paradigms existing today are so entrenched in technology that it's sincerely hard for people to conceive of a brand new idea. I think it's a lot like going from a car to a boat. If somebody has never conceived of a boat, they can't see how it works. My ideology here is essentially making a boat that used to run as a car—so people can understand boats.

Even for me, the developer, it was hard to shift away from everything I'd conceived for the past 20 years. The idea is deleting 50 years of existing architecture: everything from TCP stacks to the operating system itself, even UIs and hardware development concepts. But luckily, we're in 2025. We have FPGAs, modern compilation routines, and AI that can help us explore these paradigms without wasting as much time as we would have 20 years ago.

So let me tell you how I got here, and why I think this alternative paradigm is worth exploring.

---

## Where This Started: The Alternative Bunny

Throughout my life—being autistic as I am—I've always felt on the outer fringe of society. This coupled with my technical work created an interesting pattern: where one person would pick the most popular framework, I would invest time in the third most popular. Not for any practical reason. Just to be different.

For a very long time, I've wanted to research alternative concepts. As a youth, I was into alternative sciences. Like every child geek, I thought maybe I could solve perpetual motion and change the world. I failed pretty quickly, of course. But as a "miniature scientist," I took time to invest in understanding elements people overlooked. Eventually, I gravitated toward mathematics—specifically graph theory, which is itself an alternative paradigm to standard mathematics. I felt calculus was boring, so I moved on to alternatives.

### Early Computing: VB6 and Downloaded Wikipedia

My computing education started late. I was 16 when I got my first PC. Before that, I'd been interested in binary logic and standard notation, but couldn't actually do anything with it. When I finally got internet access (AOL dial-up, if you remember those days), the first thing I did was spend far too much time downloading half of Wikipedia. Back then, it was just full of intrinsic ideas put together by geeks—a real treasure trove for research.

Perusing through technologies, new ideas, Egyptians, UFOs, and top-secret information, I stumbled across programming languages. My first study became web development because it was accessible. I could do HTML, CSS, and JavaScript without bugging anybody. I could sit alone and study.

My first proper programming environment was VB6—predominantly because it was already on the machine and ready to go. I loved all the stuff Microsoft did. MSDN could be installed from a disk. It was a wonderful way to access programming documentation.

I felt the best way to learn was to find a hard problem and try to write it myself. Because I was intrinsically a programmer. Ever since I touched those buttons, I wanted to program. I looked at the programming interface kind of like how an artist looks at a blank canvas and thought: *I can do absolutely anything here.*

In VB6, it was great to build UIs, interfaces, little save files. But to explore more advanced technologies, I had to pick hard things to program. So I'd start with hard problems and struggle through them.

**My end goal, right from the beginning: I'd love to make my own operating system.** Right from the core. I wanted to understand all the technologies under the hood—from bit to byte, from "what happens when you turn the computer on?" to how applications actually execute.

That study led me into operating system development. But of course, me being the alternative bunny I am, I mixed it up: What's the brand new operating system I can invent in an alternative paradigm?

Twenty years later, here we are.

---

## The Winding Path: Army, Adobe, Analytics, and Corporate Life

Let me give you the condensed career history, because it matters for understanding how I approach this work.

### Military and College (Never Finished)

I started out in the army. When you're young, they put you through additional education, and I said I'd like to do computing. So while doing army work, I went to college part-time studying computing (A-levels, O-levels, GMVQs, NVQs—the whole alphabet soup). 

I never completed most of them. The problem wasn't ability—I'd already exceeded what college taught. At 16 or 17, I found myself walking around classes showing people how to program. I got bored quickly. And in my first attempts at education, I didn't even have a computer—I had to submit all my work handwritten. Which sounds crazy today, but hey, I didn't have a computer and I wanted to answer the questions.

### The Adobe Years (Train to Scotland)

On the day I left the army, I was sitting on a train heading to Scotland to visit my girlfriend. The guy opposite me was interested in what I was doing. He mentioned he was working with Flash—a design interface I'd started playing with. Over the previous couple of years, I'd gotten into animation and AS3 programming (ECMAScript-based, easy to pick up after JS).

By happenstance, this person worked for Adobe. He became a national/international trainer teaching AS3, and through that connection, I spent years as a developer teaching people to program and animate. That was fine until Apple killed the Adobe suite.

### Freelancing, Analytics, and an Uncomfortable Realization

After Adobe, I freelanced. Got a lot of work, comfortable for years—until the credit crisis dried everything up. During that period, I worked on graphical interfaces, socket communications (ships, land-based systems), and analytics for counting people in large areas. I won a few prizes.

Then the software was sold to Palantir.

I didn't realize back then what they would do with it. Since then, I've looked back at my life and tried to understand: the things I build may always end up in areas I wouldn't want. **That realization changed me.** I felt my best way forward was to keep my head down and work quietly.

### Corporate Life and Background Obsession

For the past decade or so, I've worked in corporate environments—web development, teaching, typical work. It's been quiet. But beneath the surface, every day, every month, every year, I kept plucking at this background knowledge: *What if I made my own operating system?*

---

## The Wall: When You Need University to Build Your Hobby

More than a decade into corporate life, typing away at bland reports and general duties, I hit a serious wall. I wanted to build a graph engine for computation, and for more than a year, I struggled. I couldn't do the math. I couldn't understand what I was building—not the theory, not the physics, not the graphics computations.

So I went to university.

I signed up as an external adult student, long-distance learning. Then COVID happened. Perfect timing, really—I spent those years inside studying mathematics while the world locked down. I focused on graph theory specifically, wanting something more intrinsic to nature than standard programming paradigms.

I quickly discovered an aptitude for more complex mathematics. **And immediately, it paid dividends in my operating system work.** Through my mathematical education, I could implement ideas directly into the Virtual Operating Layer. The feedback loop was incredible—as soon as I learned something, I could apply it to my architecture.

One example: **Hyperway**, a graph execution library I built in Python as part of my coursework. It is phenomenal. It works great. But it's also the product of **40 different rewrites** across **25 fundamental ideas** that I deleted and restarted.

That's my development philosophy in a nutshell.

---

## My Development Method: Perpetual Rewrites

One of the methods I use to re-educate myself and ensure I write the best code I can: once I've written something—finished or even halfway through—I stop and ask myself, *"Is this the best I can produce? Have I hit any problems, barriers, or bugs?"*

If I have, or if I'm not 100% happy with the work, that's fine. This is my education time. **I just start again.**

As a result:
- **Hyperway**: 40 rewrites, 25 fundamental frameworks
- **Virtual Operating Layer**: A "smash of mess" in the source code, years of creating and deleting and destroying ideas
- **This is probably the 10th attempt** at writing a kernel core

Each time I start over, I simplify. Eventually, the base framework evolved from "its own operating system" to "a layer on top of existing operating systems." At the moment, I don't know how to build a kernel properly, so I'll borrow from the great Linux frameworks.

### Why a Layer, Not a Full Kernel

This is one of my bugbears: I've always tried to focus on both Linux and Windows. But when you look at most "new" operating systems, they're not actually their own operating system. The kernel is a Unix base, a POSIX base, a DOS base, or some other borrowed kernel. They haven't been invented from the core.

I wanted all my learning to be true. That's why it became an **operating layer**—the first attempts will live on top of the user's preferred host.

And by accident, this aligns perfectly with modern trends. Today it's standard to have sublayers: Windows Subsystem for Linux, Docker containers, VirtualBox, Oracle VM, extensive sandboxing. **This dissection of concepts should exist right in the core.** It's not a limitation—it's a design feature.

---

## Understanding What We're Replacing: Von Neumann Architecture

Before we can talk about alternatives, we need to understand what we have.

All modern computing rests on **Von Neumann architecture**. For those unfamiliar, here's the fast description: you'll quickly realize you *do* know what it is because it's built so intrinsically into technology. It's almost as if wood were made of trees and cars were made of metal—it's fundamental to how we think about computing.

### The Traditional Model

Under the hood, we have:
1. **Data stored somewhere** (disk, memory)
2. **A CPU that executes instructions**
3. **An execution environment** (like a word processor)

The word processor plucks data off your disk and prints it on the screen in a very special manner. One of the things I've always wanted to do is simplify things so I understand them. And when you simplify computing to its core: **everything is just bits and bytes.**

We pull a bit, manipulate it, and put it on the screen. It doesn't matter if this is a computer game or a word processor. All we're really doing is manipulating core bits and converting them to other core bits. We make **patterns of light on display units** that we interpret as meaningful. Those particular patterns of light are the letter "F," for example.

```
┌─────────────────────────────────────────┐
│  Traditional Von Neumann Architecture   │
├─────────────────────────────────────────┤
│                                         │
│  Storage (Disk) ──→ Memory (RAM)       │
│         ↓                               │
│    CPU Execution                        │
│         ↓                               │
│    Output (Display)                     │
│                                         │
│  Linear, Sequential, Separated          │
└─────────────────────────────────────────┘
```

This model has served us for 50+ years. But what if we started fresh?

---

## The Alien Thought Experiment: Starting from Zero

Here's a thought experiment I return to constantly:

**If I strip away all the human baggage—the whole files, folders, desktops thing—what would an operating system actually look like?**

If an alien turned up, completely outside our cultural habits, what sort of interface would they build?

The alien analogy helps me step out of the human vessel for a moment. It lets me think holistically. If someone had never seen our UI history, never seen a window or a menu bar, what would they invent? What would be the natural way to interact with a machine?

**Because at the end of the day, an OS is the translator between raw binary and the human experience—between machine language and something visual or emotional for us.** So maybe the future interface isn't files and folders at all. Maybe it's something more fluid, or geometric, or graph-based, or something we haven't even described yet.

And this is where all the sci-fi interfaces come to mind—Star Trek, those LCARS panels. Not literally those designs, but the idea that the UI could be something far more expressive and more native to human intuition. Something closer to how we actually think.

**Instead of starting with "What do computers do now?" we ask, "What should computing feel like if we were designing it today from scratch?"** That's the approach I'm taking with VOL. It's not just a UI rethink—it's an entire reimagination of how humans and machines communicate.

To explore this, I broke the problem into three parts:
1. **The graphical interface** (how humans interact)
2. **The backend/hardware componentry** (how machines process)
3. **The software layer/OS itself** (how we bridge the two)

So there's more than just an operating system here—it's a re-understanding of how we interact with computing at a fundamental level.

### The Machine-Human Bridge

An alien would show us a closer communication of how things execute, how they run, how they can be explored versus how they touch the physical world. This leads into **graph theory**—what I see as more of an explanation of the natural world, akin to pure mathematical understanding.

The exploration also involves **conformal geometric algebra (CGA)**—almost alien mathematics that exists today but rarely gets attention because of classical physics dominance. As the alternative bunny, I dove deep into CGA and related frameworks.

These types of mathematics give us more guidance toward holistic mathematical operations. Question: **If we delete for a moment the concept of traditional operators, what type of math would the CPU build?**

That question led me to research what others have done in the past to challenge conventional perspectives.

---

## Historical Context: Others Who Questioned Everything

I'm not the first person to look at this. Throughout computing history, there have been radical departures:

### The Lisp Machine Era
In the 1970s-80s, companies like Symbolics built **Lisp machines**—computers designed from the ground up for symbolic computation. Everything from the hardware to the OS was optimized for Lisp. They represented a complete rethinking of the hardware-software boundary.

### Xerox PARC and Smalltalk
The Smalltalk environment wasn't just a language—it was an entire computing paradigm. Everything was an object. Everything sent messages. The entire OS was written in Smalltalk and could be modified at runtime. It fundamentally questioned the separation between "system" and "user" code.

### Connection Machines and Dataflow
In the 1980s, Danny Hillis built the Connection Machine—massively parallel computers with 65,536 processors. It represented a complete departure from sequential Von Neumann architecture. Similarly, **dataflow architectures** explored computation where instructions execute as soon as their inputs are available, not in a predetermined sequence.

### Actor Model and Erlang
The Actor Model (and its implementation in Erlang) showed that message-passing between isolated processes could be a fundamental computing primitive. No shared memory, no locks—just actors sending messages. It's proven remarkably resilient and scalable.

### Capability-Based Systems
Systems like KeyKOS and EROS explored **capability-based security**—where access rights are unforgeable tokens you pass around, rather than ambient authority checked by permission systems. The OS enforces security through object references themselves.

### What They Taught Me

These historical explorations showed me that **alternative paradigms are possible**. More importantly, they showed patterns:
- Most failed commercially but influenced later systems
- Technical elegance doesn't guarantee adoption
- The transition cost from existing systems is enormous
- But the ideas persist and reemerge when technology catches up

That's why VOL is an **operating layer** first. I'm not asking people to abandon everything—I'm building a bridge.

---

## The Multi-Paradigm Reality We Already Live In

Here's something I've been thinking about a lot: **we already have multiple computing paradigms coexisting today.**

When we look at all these other approaches—like GPUs having their own architecture, or quantum computing running under completely different rules—it shows we don't actually need to stick to one paradigm. We already have multiple paradigms coexisting today, but we still force everything through this classical Von Neumann pipeline.

### Different Architectures, Same Old OS

Think about it:
- **GPUs** don't behave like CPUs
- **TPUs** don't behave like GPUs  
- **Quantum machines** operate under fundamentally different principles
- **FPGAs** can be reconfigured to implement custom logic
- **NPUs** (Neural Processing Units) optimize for AI workloads

And yet all of that still ends up being controlled by a classical operating system that only understands one style of execution. We treat these as special cases, as exceptions to the rule, as things you access through libraries and APIs.

**But what if we didn't?**

If we had the ability to mix those paradigms right at the operating system level—not bolted on top as a library—then we could actually create something more flexible. **A system that isn't locked into "execute line one, then line two," but can branch and merge the way natural systems do.**

### The Direction Forward

That's the direction I'm pushing toward: making an architecture that can adapt and work with these different forms of computation instead of always forcing everything into the same old model.

It's not really about wrapping anything up—it's about finally seeing the pattern. When you look at where computing is going, we already have these different paradigms running side by side. Even quantum machines end up being controlled by a classical operating system that only understands one style of execution.

**So if we take that idea seriously—that computation already has multiple architectures—then why shouldn't the operating layer itself be built to support that?**

Instead of forcing everything into one execution model, the system should be able to adapt to whatever kind of processing is happening. That's the whole point of what I'm doing: **shifting the architecture so it can natively handle these different ways of working, instead of treating them as exceptions or special cases.**

```
┌──────────────────────────────────────────┐
│   Traditional OS Architecture            │
├──────────────────────────────────────────┤
│                                          │
│  Classical OS (Von Neumann)              │
│         ↓                                │
│    [CPU] [GPU] [TPU] [QPU]               │
│     All accessed as special cases        │
│     through libraries & APIs             │
│                                          │
└──────────────────────────────────────────┘

┌──────────────────────────────────────────┐
│   VOL Multi-Paradigm Architecture        │
├──────────────────────────────────────────┤
│                                          │
│  Graph-Based OS Layer                    │
│    Natively supports multiple            │
│    execution paradigms                   │
│         ↓                                │
│    [CPU] ←→ [GPU] ←→ [TPU] ←→ [QPU]     │
│     All first-class citizens             │
│     in the execution graph               │
│                                          │
└──────────────────────────────────────────┘
```

---

## The Virtual Operating Layer: Core Concepts

Now let's talk about what I'm actually building.

As a caveat: **it's still in progress.** It'll take forever to build, and I don't think we'll ever truly be "done." But the ideas are driving toward what I call "the machinery which should have been."

### 1. Graph Theory as Foundation

The fundamental shift: **walking away from the idea that bits just sit in memory.**

No hard drive platters. No separated RAM and storage points. We emerge from those constraints and ask: what's the most ideologic system we can build?

The concept recognizes that **data transfer is fast now**. Modern NVMe drives deliver 12+ GB/s. We won't have the limitations of the past—waiting for bit transfers. We no longer need to work in 4KB segments. We can work with 10MB chunks if we want. Computing today can handle it.

**The interface itself should be graph nodes.** There are no files and folders in the traditional sense. The bits coalesce for us. They're part of an intrinsic data space that we as users should be able to access and flow through.

> **We shouldn't have to organize. We should just have to utilize.**

In our real world, when things are prepared, they *are*—they exist in a state of being. These things need to exist in that same way when we use them.

```
┌─────────────────────────────────────────┐
│    Graph-Based VOL Architecture         │
├─────────────────────────────────────────┤
│                                         │
│         Node A ←──→ Node B              │
│           ↓ ↖         ↓                 │
│         Node C ←──→ Node D              │
│           ↓           ↓ ↖               │
│         Node E ←──→ Node F              │
│                                         │
│  Connected, Self-Executing, Parallel    │
└─────────────────────────────────────────┘
```

### 2. Self-Executing Code

Part of the concept is **self-executing architecture**. In the current world, we have userland and safety prioritized by segmentation and permissions. But starting from scratch, what does the user even execute?

We still need segmented portions of our data space (I'm just calling it "space" from now on). We need to segment space relative to both the work and the users. Multiple people might utilize one space.

**Thankfully, graph theory gives us the architecture built-in.** When you're walking a graph, you cannot exit a graph unless you have a path outside the graph. **A graph is self-enclosed.** This is a fundamental mathematical property we can apply directly.

---

## Security Through Topology: The Cup Metaphor

Here's where it gets interesting.

What if when we execute code, we work at a graph node—and you cannot escape that node except through defined paths? You can only access the bits you've been given connections to reach.

We'll still work in bits (fundamentally, that can't change—we'll always work in bits). But I like to think of these bits as little particles, little ASCII characters.

### The Physical Analogy

In a paradigm where code is self-executing, this is like the real world. **If you pick up a thing, it is part of that thing.**

If I have a cup, it is either:
- A full cup
- Parts of a broken cup
- But always: previously cup componentry

Under the hood, it's a graph of particles all built together. They're all similar particles, but when they **collate**, when they become part of this cup, it is always cup-like. We define it as such.

The same architecture applies to code execution:
- When we execute things on the CPU, we **walk a graph of defined bits**
- When those bits are working, they're understood to be **part of their being**
- The cup is a cup, my keyboard is a keyboard
- Data bits that flow through—text, video RAM, keyboard inputs—are **bits of execution defined by their states**

At the moment, this is hard to conceptualize. But understand: **there's no traditional file system here. It's fully abstract.** We pick up particles, move them into a place, and bind them together to invent a thing.

The same applies to a graph.

---

## Permissions Without Permission Systems

Here's the profound implication: **I envisage we won't have permissioned bits**, or at least not in the same manner as today.

In theory, we would never give a user the capability to execute bits they haven't graphed. Their userland—**the space they are walking**—is always set such that they cannot walk out of that environment and step on dangerous bits.

> **Permissions shouldn't need to exist because the graph itself will only be built for that user.**

In a world where the kernel drives more of userland space, when a user requests their bits, those bits are **arranged for that user**. If they want to discover other bits not part of their user space, they must first **build a path to those bits**—just as graph theory requires.

### Traditional vs. Graph Security

```
Traditional Permissions:
┌────────────────────────────────┐
│ User tries to access file      │
│      ↓                         │
│ OS checks permission bits      │
│      ↓                         │
│ Allow or Deny                  │
└────────────────────────────────┘

Graph Security:
┌────────────────────────────────┐
│ User walks graph               │
│      ↓                         │
│ Can only follow existing edges │
│      ↓                         │
│ Unreachable nodes don't exist  │
│   (from user's perspective)    │
└────────────────────────────────┘
```

It's security through **topology**, not through permissions checking.

---

## Example: Walking the Bluetooth Stack

Let me make this concrete with a real-world example.

I always think of the **Bluetooth stack** as a good mental model. It has many procedural wait-and-return commands. It runs asynchronously. It needs to pause and wait for responses. It's perfect for exploring graph execution.

### Traditional Approach

In a traditional system, you'd have a file of code running procedurally:

```c
// bluetooth_driver.c
void init_bluetooth() {
    power_on_radio();
    wait_for_ready();
    scan_for_devices();
    // ... hundreds of lines ...
}
```

The entire file is an execution state run by the processor, line by line.

### Graph Approach

In the graph model, you **split the Bluetooth stack into smaller nodes**. Each node actuates a small piece of code.

Think of it like that C file with many lines—but rather than providing the entire file to the processor, when the **worker** or **stepper** walks our graph and hits a particular line, it:
1. Executes that line
2. Waits for or walks to the next node

You could split the file into many nodes and achieve the same behavior.

### But Here's the Power

Entrenched in the enhanced abilities of graph theory, we can **add additional paths** from similar nodes to execute truly parallel work.

```
┌─────────────────────────────────────────────┐
│  Bluetooth Graph Execution                  │
├─────────────────────────────────────────────┤
│                                             │
│  [Power On Radio] ──→ [Wait for Ready]     │
│         ↓                    ↓              │
│    [Log Event]        [Scan Devices]       │
│         ↓                    ↓              │
│  [Update UI] ←──────── [Process Results]   │
│                                             │
└─────────────────────────────────────────────┘
```

A line in code could **both**:
- Call out to the Bluetooth stack to turn it on
- Print a log file
- Move on to the next stack node

All simultaneously, following different graph edges.

**This concept should drive every single execution in the OS, right at the core.** We delete the idea of linear execution of lines in a particular file and instead write graphs where each step performs a small execution of work.

---

## The Passion Project: WebSockets and Perpetual Learning

I need to tell you about my obsession with WebSockets.

One of my all-time passions, for some ungodly reason, is **WebSockets**. I love them to death. Every month or every year, I'll have another go at rewriting a WebSocket implementation.

Why? It's part of my development method to re-educate myself and ensure I write the best code possible. My process:

1. Write something (finished or halfway)
2. Stop and ask: *"Is this the best I can produce? Have I hit problems, barriers, or bugs?"*
3. If yes, or if I'm not 100% happy: **start again**

This is my education time, so starting over isn't failure—it's iteration toward understanding.

As I progressed through my mathematics education, I explored:
- File systems
- Graphics engines
- Game development
- Real-time operations

I already had grounding in **web real-time sockets**—that's where my interests naturally lie. The intersection of real-time communication, async operations, and protocol design is endlessly fascinating to me.

---

## Current State: Components of VOL

So what actually exists right now?

### Hyperway
A **graph execution library** built in Python. Developed during my university coursework. It is phenomenal—it actually works. Product of 40 rewrites across 25 fundamental frameworks.

### Polypoint UI
A user interface that reimagines how humans interact with graph-based systems. Still in development, but exploring natural interaction patterns.

### BuildRoots Integration
Allowing me to compile custom Linux bases until I'm ready to build my own kernel. This is the "scaffolding" layer—proving concepts on stable foundations before going deeper.

### VOL Core (In Progress)
The operating layer itself. A "smash of mess" in the source code—years of creating, deleting, destroying, and rebuilding ideas. This is probably the 10th fundamental attempt at the kernel concepts.

---

## Why This Matters: The Machinery Which Should Have Been

You might ask: **Why go through all this?** Why spend 10 years rebuilding computing from scratch when perfectly good operating systems exist?

A few reasons:

### 1. Potential Performance Gains
Graph-based execution with true parallelism could be significantly faster for many workloads. Modern hardware is massively parallel—our software should be too.

### 2. More Natural Security Model
Security through topology is elegant. No permission bits to check, no ambient authority to exploit. You simply cannot access what you cannot reach through the graph.

### 3. Better Human-Computer Interaction
By rethinking the interface layer alongside the execution layer, we can create more natural ways for humans to interact with computation. Not files and folders—flows and spaces.

### 4. Mathematical Foundations
Using graph theory, conformal geometric algebra, and other mathematical frameworks provides a **rigorous foundation**. The system's behavior derives from mathematical properties, not accumulated hacks.

### 5. Learning and Understanding
Even if VOL never becomes a production OS, the exploration teaches us about computing. Questioning assumptions. Understanding what's essential versus what's historical accident.

### 6. Inspiration for Others

This is the big one for me. **My goal is to sincerely try to offer the ideas and concepts, hopefully sparking the same passion in others.**

I want other developers to look at this and think: *"Wait, we could do it differently?"* To give themselves permission to question 50 years of computing history and ask, *"But what if we didn't do it that way?"*

---

## The Ethics of Building

I need to address something that shaped how I approach this work.

During my freelancing years, I built analytics software for counting people in large areas. I won prizes. The software was eventually sold to Palantir.

**I didn't realize back then what they would do with the software.**

That realization haunts me. The things I build may end up in areas I wouldn't want. It forced me to think about **why** I build and **for whom**.

The Virtual Operating Layer is different. It's:
- **Open source** (no hidden proprietary use)
- **Research-focused** (understanding over exploitation)
- **Community-driven** (not corporate-controlled)
- **Educational** (explicitly meant to teach and inspire)

I'm building this not because someone will pay for it or weaponize it, but because **I want to understand**. And I want to share that understanding with others who might use it better than I can imagine.

---

## Technical Challenges and Honest Limitations

Let me be transparent about the challenges:

### 1. I Don't Know How to Build a Kernel Properly
That's why it's an operating **layer** first. I'm borrowing from Linux until I understand kernel development deeply enough to do it from scratch.

### 2. The Graph Execution Model Is Hard to Debug
When everything is parallel and graph-based, traditional debugging tools don't work well. I'm still figuring out how to make this developer-friendly.

### 3. Performance Might Not Beat Optimized Traditional Systems
Modern OSes have 50 years of optimization. Even if the graph model is theoretically faster, beating decades of engineering is hard.

### 4. Adoption Is Nearly Impossible
The transition cost from existing systems is enormous. That's why I'm focused on **ideas** more than market adoption.

### 5. I Might Be Wrong
About everything. The whole approach might be fundamentally flawed. That's okay—exploration is valuable even when it fails.

---

## Tools for Exploration: Why Now?

Twenty years ago, this project would have been impossible. Today, we have:

### FPGAs and Custom Hardware
Field-Programmable Gate Arrays let us experiment with hardware-level changes without manufacturing custom silicon. We can test alternative CPU designs.

### Modern Compilation Technology
LLVM, JIT compilation, and modern compiler frameworks let us experiment with execution models without writing everything in assembly.

### AI Assistants
Tools like GitHub Copilot, ChatGPT, and others accelerate exploration. They can't design the system, but they can handle boilerplate and help debug.

### Virtualization and Containerization
We can test OS concepts in isolated environments without risking the host system. Docker, VMs, and WSL2 make experimentation safe.

### Mathematical Computing Tools
Python libraries (NetworkX, NumPy, SciPy), Julia, and other modern tools make graph theory and complex mathematics accessible.

### Open Source Everything
Standing on the shoulders of giants—Linux, BSD, LLVM, countless libraries. I don't have to build everything from scratch.

**The timing that was wrong 20 years ago may finally be right.**

---

## How You Can Get Involved

The Virtual Operating Layer is open source and available for exploration. Here's how you can engage:

### 1. **Explore the Concepts**
Read the documentation. Question the assumptions. Tell me where I'm wrong—seriously, I want to know.

### 2. **Experiment with Hyperway**
The graph execution library is functional. Try building something with it. See if the model makes sense for your problem domain.

### 3. **Contribute Ideas**
Graph-based security, alternative execution models, mathematical foundations—these are huge topics. Bring your expertise.

### 4. **Build Alternatives**
Don't like my approach? Build your own! The goal is exploration, not a single "correct" answer.

### 5. **Teach and Share**
If these ideas resonate, share them. Write about them. Build on them. The more people questioning assumptions, the better.

---

## Conclusion: The Operating System That Shouldn't Exist

The Virtual Operating Layer probably shouldn't exist. It requires deleting everything we know about computing. It challenges 50 years of engineering. It's built by one person who openly admits he doesn't know how to build a kernel properly.

But it **does** exist. And it works (mostly). And it represents something increasingly rare in software development: **genuine rethinking from first principles**.

In an era where most development involves assembling pre-existing frameworks, where "innovation" means slight variations on established patterns, VOL asks a different question:

**What would computing look like if we started fresh?**

Not necessarily better (though potentially faster). Not necessarily more practical. But **different**—an alternative path that computing could have taken if different questions had been asked at the beginning.

I look at the programming interface like an artist looks at a blank canvas and think: **absolutely anything is possible.**

That's what I want to share with you. Not a finished product, but **permission to question everything**. Permission to be the alternative bunny. Permission to spend a decade building something that shouldn't work—and discovering that maybe, just maybe, it does.

---

## Resources and Further Reading

### Virtual Operating Layer
- **GitHub Repository**: [github.com/Strangemother/Virtual-Operating-Layer](https://github.com/Strangemother/Virtual-Operating-Layer)
- **Documentation**: See `docs/` directory for concept papers
- **Hyperway Library**: Graph execution framework (Python)

### Influential Historical Systems
- **Lisp Machines**: Symbolics, LMI, Texas Instruments
- **Smalltalk**: Xerox PARC, Squeak, Pharo
- **Erlang/OTP**: Actor model implementation
- **KeyKOS/EROS**: Capability-based security

### Mathematical Foundations
- **Graph Theory**: NetworkX, graph algorithms
- **Conformal Geometric Algebra**: [bivector.net](https://bivector.net)
- **Dataflow Architectures**: Historical research papers

### Modern Tools
- **LLVM**: Compiler infrastructure
- **Jupyter Notebooks**: Exploratory computing
- **Docker/WSL**: Safe experimentation environments

---

**This is a work in progress. Ten years in, with many more to go. Join me on the journey.**

*Article last updated: December 2025*

---

*If you've read this far, you're exactly the kind of person who might find this interesting. Reach out. Question the assumptions. Build something weird. Be the alternative bunny.*

*— Strangemother*
