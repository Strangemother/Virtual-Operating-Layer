# The Operating System That Shouldn't Exist

## How one developer spent a decade reimagining computing from scratch—and why it might actually work

---

In a modest corporate office somewhere in Britain, a web developer was typing away at bland reports and general duties. But in the background, something extraordinary was taking shape. For more than a decade, he had been quietly dismantling 50 years of computing architecture in his mind, rebuilding it from first principles. The result is the Virtual Operating Layer—an operating system that challenges everything from TCP stacks to user interfaces, from memory management to the fundamental Von Neumann architecture that powers every computer you've ever used.

The project recently caught the attention of technology researchers for its radical departures: alternate binary-to-trinary systems, the complete deallocation of traditional memory types and data structures, and most intriguingly, the idea that it could actually work. Unlike many theoretical computer science exercises, this one comes with a user interface called Polypoint, backend concepts in VOL, and even a BuildRoots project for compiling Linux bases—scaffolding for the day when the developer is ready to write his own kernel.

The key driver, he explains, is speed. But getting there requires something more difficult than raw performance optimization: it requires convincing people to see computing differently.

---

## The Boat That Used to Be a Car

"One of the problems is that the concepts and paradigms existing today are so entrenched in technology, it's sincerely hard for people to conceive of a brand new idea," the developer explains. "I think it's a lot like going from a car to a boat. If somebody has never conceived of a boat, they can't see it work. My ideology here is essentially making a boat that used to run as a car in order for people to understand boats."

It's an apt metaphor. The challenge isn't just technical—it's conceptual. Even the developer himself struggled to shift away from everything he'd learned over 20 years of programming. The idea, after all, is deleting half a century of architecture: everything from the operating system itself to how hardware is developed. Even user interfaces need complete rethinking.

But this is 2025, and the timing may finally be right. FPGA technology, modern compilation routines, and AI assistants can help explore alternative paradigms without the time waste that would have made such a project impossible 20 years ago. The tools to build a boat—to continue the metaphor—are finally available.

---

## The Alternative Bunny

Understanding the Virtual Operating Layer requires understanding its creator. Throughout his life, being autistic, he's felt on the outer fringe of society. That perspective extended to his technical work. Where others would pick the most popular framework, he'd invest time in the third most popular—for no other reason than to be different.

"I've always wanted to research alternative concepts," he says. As a youth, he was into alternative sciences. Like many child geeks, he thought he could solve perpetual motion. He failed quickly, but the process taught him to look at elements others overlooked. He became what he calls "a miniature scientist," gravitating eventually toward graph theory—itself an alternative paradigm to standard mathematics. "I felt calculus or something else was boring. So I moved on to an alternative."

His computing education started late. He was 16 when he got his first PC. Before internet access at home, he'd spent considerable time with AOL dial-up downloading half of Wikipedia—back when it was full of intrinsic ideas put together by geeks. Perusing through technologies, new ideas, Egyptians, UFOs, and top-secret information, he stumbled across programming languages.

Web development became his entry point because it was accessible. He could do HTML, CSS, and JavaScript alone, without bugging anybody. His first proper programming environment was VB6—simply because it was already on the machine. "I looked at the programming interface kind of like how an artist looks at a blank canvas," he recalls. "I thought to myself, what can I do here? It's absolutely anything."

His learning method was simple: find hard problems and struggle through them. From the beginning, he had one overarching goal: "I'd love to make my own operating system. Right from the core. I really truly wanted to understand all the technologies under the hood, from bit to byte, what happens when you turn the computer on?"

Twenty years later, he's writing about how he put that together.

---

## From Army Technician to Adobe Trainer to Corporate Developer

The path was circuitous. He started in the army, where they put young recruits through additional education. "I'd like to do computing," he told them. While doing army work, he attended college part-time, studying A-levels, O-levels, GMVQs, and NVQs—though he never completed most of them. The problem wasn't ability; it was boredom. He'd already exceeded what college taught. At 16 or 17, he found himself walking around classes showing others how to program. In his first attempts at formal education, he didn't even have a computer—he had to submit all his work handwritten.

On the day he left the army, serendipity struck. Sitting on a train to Scotland to visit his girlfriend, the man opposite him mentioned he was working with a program called Flash. The stranger worked for Adobe and soon became a national trainer teaching AS3 programming. Through that connection, the developer spent years teaching others to program and animate—until Apple killed the Adobe suite.

Freelancing followed. The work was good until the credit crisis dried it up. During that period, he worked on graphical interfaces and socket communications—ships, land-based systems, analytics for counting people in large areas. He won prizes. Then, to his dismay, the software was sold to Palantir. "I didn't realize back then what they would do with the software," he reflects. "Since then, I've looked back and tried to understand—the things I build may always end up in areas I wouldn't want. As such, I felt my best way forward was just to keep my head down."

For the past decade, he's worked in corporate environments, quiet and typical. But beneath the surface, that question kept plucking at him: what if I made my own operating system?

---

## The Wall and the University

More than a decade into his corporate career, he hit a wall. To progress his OS, he needed to build a graph engine for computation. For more than a year, he struggled. He couldn't do the math, couldn't understand the theory, the physics, the graphics. So he did what he'd always done when faced with a hard problem: he studied.

He signed up as an external adult student, long-distance. Then COVID happened. He spent those years inside, studying mathematics—specifically graph theory. "I quickly discovered an aptitude for more complex mathematics," he says. The decision paid dividends immediately. Through his mathematical education, he could implement ideas directly into the Virtual Operating Layer. 

One example is Hyperway, a graph execution library built in Python that he developed as part of his coursework. "It is phenomenal. It works great." But Hyperway represents more than just success—it's the product of 40 different rewrites, 25 fundamental ideas deleted and restarted. The same pattern applies across his work. The Virtual Operating Layer's source code is "a smash of mess," years of creating, deleting, and destroying ideas. This version is perhaps the tenth attempt at writing a kernel core.

Each time he starts over, he simplifies. Eventually, the base framework became not its own operating system but a layer on top of existing operating systems. "At the moment, I don't know how to build a kernel properly," he admits candidly, "and as such, I'll borrow from some of the great Linux frameworks."

This decision proved prescient. By accident, it aligns perfectly with modern computing trends: sublayers in Windows, virtual boxes, Oracle boxes, extensive sandboxing. "This dissection of concepts should exist right in the core," he argues. It's not a compromise—it's a feature.

---

## Bits, Bytes, and Patterns of Light

To understand what makes the Virtual Operating Layer different, you first need to understand what it's replacing. At its foundation, all modern computing rests on Von Neumann architecture—a design so intrinsic to technology that we barely notice it. It's "almost as if wood were made of trees and cars are made of metal," the developer explains. We have data stored somewhere. When we want to use it, we execute it with a CPU and an execution environment like a word processor. The word processor plucks data off disk and prints it on screen in a very special manner.

"To simplify computing, everything is just bits and bytes," he says. "We pull a bit, manipulate it, and put it on the screen. It doesn't matter if this is a computer game or a word processor. All we're really doing is manipulating core bits and converting them to other core bits. We make patterns of light on display units that we make sense of. Those patterns of light there in particular are the letter F, for example."

It's both reductive and profound. If you strip away decades of accumulated complexity, that's what computing is: bit manipulation and light patterns that humans interpret as meaningful.

But what if you started from scratch? What if an alien civilization came to Earth with their operating system ideas—what would they say?

---

## The Alien OS

This thought experiment runs throughout the developer's work. If you were a being that understood everything about humanity and technology but had never seen a computer, what kind of interface would you build?

"If I strip away all the human baggage—the whole files, folders, desktops thing—what would an operating system actually look like?" he asks. "If an alien turned up, completely outside our cultural habits, what sort of interface would they build?"

The alien analogy helps him step outside human preconceptions for a moment, to think holistically. If someone had never seen UI history, never seen a window or a menu bar, what would they invent? What would be the natural way to interact with a machine?

"Because at the end of the day, an OS is the translator between raw binary and the human experience—between machine language and something visual or emotional for us. So maybe the future interface isn't files and folders at all. Maybe it's something more fluid, or geometric, or graph-based, or something we haven't even described yet."

When we look at Star Trek and those LCARS panels, the question isn't about copying those designs literally—it's about recognizing that the UI could be something far more expressive and more native to human intuition. Something closer to how we actually think.

We know our operating systems aren't perfect. We have problems, and they're not intrinsically useful to all humans. Could AI and neural networks—frameworks we didn't have the understanding to challenge in the past—point toward a different future? Could we build a platform that allows human beings to natively understand what's occurring?

"Instead of starting with 'What do computers do now?' we ask, 'What should computing feel like if we were designing it today from scratch?' That's the approach I'm taking with VOL. It's not just a UI rethink—it's an entire reimagination of how humans and machines communicate."

To explore this, he broke the problem into three parts: the graphical interface (how humans interact), the backend hardware componentry (how machines process), and the software layer itself (how we bridge the two). More than just an operating system, it's a re-understanding of how we interact with computers.

### Beyond UI: The Multi-Paradigm Reality

Moving beyond the interface question, there's another insight that shapes his work: we already live in a multi-paradigm computing world, even if we don't properly acknowledge it.

"When we look at all these other approaches—like GPUs having their own architecture, or quantum computing running under completely different rules—it shows we don't actually need to stick to one paradigm," he explains. "We already have multiple paradigms coexisting today, but we still force everything through this classical Von Neumann pipeline."

GPUs don't behave like CPUs. TPUs don't behave like GPUs. Quantum machines operate under fundamentally different principles. And yet all of that still ends up controlled by a classical operating system that only understands one style of execution.

"If we had the ability to mix those paradigms right at the operating system level—not bolted on top as a library—then we could actually create something more flexible. A system that isn't locked into 'execute line one, then line two,' but can branch and merge the way natural systems do."

This is the direction he's pushing toward: making an architecture that can adapt and work with these different forms of computation instead of always forcing everything into the same old model. "Instead of treating them as exceptions or special cases, the system should be able to adapt to whatever kind of processing is happening. That's the whole point: shifting the architecture so it can natively handle these different ways of working."

It's not wrapping anything up—it's recognizing the pattern that's already emerging. Computation already has multiple architectures running side by side. Why shouldn't the operating layer itself be built to support that?

The exploration also involves conformal geometric algebra (CGA) and related mathematical systems—"almost alien mathematics that exists today" but rarely gets attention because of classical physics. "If we delete for a moment the concepts of operators, what type of math would the CPU build?" It's a question that led him to discover what others have done in the past to challenge conventional perspectives.

---

## The Graph That Executes Itself

At the heart of the Virtual Operating Layer lies a radical departure: graph-based, self-executing architecture. The fundamental shift is walking away from the idea that bits just sit in memory. No hard drive platters. No separated RAM and storage points. "All these ideas—we have to emerge from that and say, what is the best or most ideologic source system that we can build?"

The concept recognizes that data transfer is fast now. Modern drives deliver 12 gigabytes per second. "We won't have the limitations of the past of waiting for transfer of bits," he argues. "We no longer need to work in four-kilobyte segments. We can actually work at maybe 10-megabyte segments, which are massive. But hey, computing today can handle it."

In this system, the interface itself is graph nodes. There are no files and folders in the traditional sense. "The bits themselves coalesce for us. They're part of an intrinsic data space that we as the user should be able to access and flow through. We shouldn't have to organize. We should just have to utilize."

It's inspired by the physical world. "In our real world, when things are prepared, they are of being. And these things need to exist of being when we use them."

---

## Security Through Topology

One of the most elegant aspects of the graph approach is how it handles security. In current systems, we have userland and safety prioritized by segmentation and permissions. But what if you started from scratch without a traditional userland?

"Thankfully, in graph theory, the architecture or the bit knowledge is kind of built in," the developer explains. "When you're walking a graph, you cannot exit a graph unless you have a path outside the graph. A graph is self-enclosed."

This mathematical property becomes the security model. What if, when executing code, you work at a graph node and cannot escape it? You can only access the bits you've been given a path to reach. "We'll still work in bits here because, fundamentally, that can't change. We'll always work in bits." But those bits are conceptualized as particles that bind together.

The physical metaphor continues: "If I have a cup, it is either a full cup or maybe parts of a broken cup. But in all cases, it was previously cup componentry. Under that hood, of course, is a graph of particles, all built together. When they collate, when they become part of this cup, it is always cup-like, and we define it thus."

The same architecture applies to code execution. "When we execute things on the CPU, we walk a graph of defined bits. When those defined bits are working, they are understood to be part of their being. The cup is a cup, my keyboard is a keyboard, and these data bits have flowed through—maybe text, maybe a video RAM component, maybe keyboard inputs. They're just bits of execution defined by their states."

---

## Permissions Without Permission Systems

The implications for security are profound. "I envisage that we won't have permissioned bits, or at least in the same manner as we do today," he says. "In theory, we would never give a user the capability to execute bits of which they haven't graphed."

In other words: your userland—the space you're walking—is always set such that you cannot walk out of that environment and step upon dangerous bits. "Permissions shouldn't need to exist because the graph itself will only be built for that user."

When a user requests their bits, those bits are arranged for that user by the kernel. If they want to discover other bits not part of their user space, they must first build a path to those bits—just as graph theory requires.

---

## Walking the Bluetooth Stack

To make this concrete, consider a device driver—say, for Bluetooth. "I always like to think of the Bluetooth stack as a good one because it has many procedural wait and return commands. It has to run asynchronously, it needs to pause, and you need to answer to it. It's a good mental model."

In a traditional system, you'd have a monolithic file of code that runs procedurally. In the graph model, you split the Bluetooth stack into smaller nodes. "Each one of those smaller nodes actuates a smaller piece of code. Think of it like a C file where you have many lines of code—but rather than providing the entire file as an execution state run by a processor, when the worker or stepper walks our graph and hits a particular line, it executes that line and waits for or walks to the next node."

You could split a file into many nodes and achieve the same behavior. But the graph architecture unlocks something more: true parallelism. "We could add additional paths from similar nodes in order to execute truly parallel work, such that a line in code could both call out to the Bluetooth stack to turn it on and also print a log file or move on to the next stack node."

This concept—splitting execution into graph nodes with multiple possible paths—should drive every single execution in the operating system, right at the core. "Finally, we delete the idea of linear execution of lines, thanks to a particular file of work, and instead look at nodes being associated with each other—i.e., writing a graph—and each step performs a small execution of work."

---

## The Passion for WebSockets and Perpetual Rewrites

Throughout his development journey, one quirk stands out: his love for WebSockets. "One of my all-time passions, for some ungodly reason, is WebSockets. I love them to death, and every month or every year I would have a go at rewriting another WebSocket."

It's part of his development philosophy. His method to re-educate himself and ensure he writes the best code possible is simple: once he's written something—a finished product or even halfway through—he stops and asks, "Is this the best that I can produce? Have I hit any problems or barriers or bugs?" If he has, or if he's not 100% happy, he starts again.

"This is my education time, so I'll just start again."

Hyperway exemplifies this: 40 different rewrites, 25 fundamental ideas deleted and restarted. The Virtual Operating Layer has been 10 years of creating, deleting, and destroying ideas. Each restart brings simplification. Each iteration brings clarity.

As he progressed through his mathematics education, he explored file systems, graphics, games, and real-time operations. He already had grounding in web real-time sockets—his natural habitat. His studies looked at everything from low-level kernel concepts to high-level interface design.

---

## Why a Layer, Not a Revolution

One might expect someone rebuilding computing from scratch to write their own kernel immediately. But he's pragmatic. "I've always felt that through my education, I've tried to focus on Linux as well as Windows. When you come across other operating systems"—he uses air quotes—"when you come across other OSs, they don't actually—they're not their own operating system. The kernel is, of course, a Unix base or a POSIX base or a DOS base. They haven't been invented from the core."

He wanted to make sure all his learning was true. That's why it became an operating *layer*. "The first attempts of the operating system will live on top of the user's preferred host. At the moment, I don't know how to build a kernel properly, and as such, I'll borrow from some of the great Linux frameworks."

Only by accident, this approach aligns with 21st-century trends. Today it's standard to have sublayers, virtual boxes, sandboxing. "This sort of conceptuality, this dissection of concepts, should exist right in the core."

It's an honest acknowledgment of both limitations and opportunities. Rather than pretending to reinvent everything at once, he's building the conceptual framework on stable foundations. The radical ideas—graph execution, self-executing code, topology-based security—can be proven on top of Linux before eventually becoming their own kernel.

---

## The Ethics of Creation

There's a haunting moment in his career story. During his freelancing years, he worked on analytics software for counting people in large areas. He won prizes for his work. The software was eventually sold to Palantir.

"I didn't realize back then what they would do with the software," he reflects. "Unfortunately, since then, I've looked back at my life and tried to understand—the things I build may always end up in areas I wouldn't want it to happen."

This awareness shaped his subsequent decade. "I felt my best way forward was just to keep my head down." For 10 years in corporate environments, quiet work. But also, 10 years of building something different. Something that he controls. Something driven not by market forces or military applications but by pure curiosity about what computing could be.

The Virtual Operating Layer represents a kind of redemption arc—technology built for the sake of understanding, for the sake of asking "what if?" without worrying about who might weaponize the answer.

---

## Tools for a New Generation

The project includes more than just the operating layer. There's Polypoint, a user interface that reimagines how humans interact with computers. There's the BuildRoots project for compiling custom Linux distributions. There's Hyperway, the graph execution library. Each piece supports the central vision: what would computing look like if we started fresh?

The developer is candid about the project's state. "As a caveat, it's still in progress. Of course, it'll take forever to build, and I don't think we'll ever get it done. But as a whole, the ideas I feel are driving toward the machinery which should have been."

That phrase—"the machinery which should have been"—captures the project's essence. Not necessarily better than what we have (though potentially faster), but different. An alternative path that computing could have taken if different questions had been asked at the beginning.

---

## Sparking the Same Passion

Why share this now? Why write about an unfinished, decade-long project that challenges fundamental assumptions most programmers never question?

"My goal is to sincerely try to offer the ideas and concepts," he explains. "Hopefully sparking the same passion in others."

There's something infectious about his approach. Not the specific technical details—though those are fascinating—but the permission he gives himself to question everything. To look at 50 years of computing history and ask, "But what if we didn't do it that way?"

In an era where most software development involves assembling pre-existing frameworks and libraries, where "innovation" often means slight variations on established patterns, the Virtual Operating Layer represents something increasingly rare: genuine rethinking from first principles.

It's the kind of project that could only come from someone who feels themselves on the outer fringe, someone who picks the third-most-popular framework just to be different, someone who thinks calculus is boring and gravitates toward graph theory instead.

Someone who looks at a programming interface like an artist looks at a blank canvas and thinks: absolutely anything.

---

## The Boat That Might Float

The challenge remains: how do you convince people to see computing differently? How do you make the boat comprehensible to people who've only ever known cars?

The developer's answer is pragmatic: you make a boat that used to run as a car. You build on Linux until you can build your own kernel. You create an operating *layer* before creating an operating *system*. You prove the concepts work before asking people to abandon what they know.

But underneath the pragmatism is something more audacious. The Virtual Operating Layer isn't just an interesting academic exercise. It's a genuine attempt to build "the machinery which should have been"—faster, more natural, more aligned with how mathematics describes the world.

Graph theory. Self-executing code. Security through topology. Conformal geometric algebra. Interfaces that flow rather than organize. Permissions that don't require permission systems. Execution that walks rather than runs linearly.

These aren't just different approaches. They're potentially transformative—if they work.

And increasingly, they might. The tooling is finally available: FPGAs for hardware exploration, modern compilers, AI assistance for rapid prototyping. The timing that was wrong 20 years ago may finally be right.

Whether the Virtual Operating Layer ultimately succeeds or fails, it serves a crucial function: it proves that alternative paradigms are possible. That someone sitting in a corporate office, typing away at bland reports, can spend a decade quietly rethinking everything—and produce something that makes researchers take notice.

It's the operating system that shouldn't exist. But it does. And that alone makes it worth paying attention to.

---

**The Virtual Operating Layer project is open source and available for researchers and developers interested in alternative computing paradigms. Documentation and source code reflect the ongoing nature of the work—ten years in, with many more to go.**

*This article represents reporting on an active research project. Technical details are current as of December 2025.*
