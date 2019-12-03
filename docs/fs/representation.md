# Represenation

+ _conceptual_

Looking further into how a custom FS will communicate with a classic appliance.
In addition the terminology or literal REPL to access the data-source.

Fundamentally a system has a core binary to run and produce a _VM_ for the FS and
its base API. The api manifests a state ready for first deployment, augmented
with future addons.

As an example of the base REPL on a tty style interface, initially "write" translates to VOL terminology as _agglomeraion of particles_ and "read" translates to colloid - to _colloid particles_.

    > AGGLOMERATE particle.reference.name content
    # Stores content as required
    > COLLOID particle.reference.name
    < PARTICLE content

A concept of 'grains' binds many particles together with a header file called a 'Phenocryst'.

    Grain:
        Phenocryst:
            id: particle.reference.name
            locations: Location references
            owner: identity
            aes: 123...
        Particle:
            content
        ...

A Phenocryst is a local cache reference stored within the VOL host. Reading 'meta data' of a 'file' may be done through the Phenocryst reference. Maybe something like:

    > PHENOCRYST OWNER particle.reference.name
    < IDENTITY identity


These are low-level calls designed for core access to the users content cloud. A floating particle may be useless without a grain and become sedimented. As such a higher-level API serves the user and applications with goruping resources of Grains and Aggregates.

An ideology of building a membrane referable Grain containg a particle.

    > GRAIN grain.reference.name AGGLOMERATE particle.reference.name
    > COLLOID grain.reference.name
    < GRAIN content

With this a high-level process can bond hemogenous particles across the membrane without manual marshalling.

    > GRAIN grain.reference.name AGGLOMERATE other.reference.particle
    > COLLOID grain.reference.name
    < GRAIN content\nother content


+ A Grain may agglomerate Particles or Grains
+ Many Grains colloid to an Aggreggate
+ An aggregate is a composed unit for processing

A REPL short syntax is viable introducing the concept of user-space short-terms. Or shortcut words a user may apply to a phenocryst for easy reference. They must be unique

    > SHORT eric particle.reference.name
    > SHORT other other.reference.particle
    > G eric A other

or even store the result of the agglomeration:

    > = eric + other

in classical form this would read `eric += other`. Further we can colloid Grains - whilst working with particles.

    > G= eric + other
    > ^+ tom.grain.flooble
    > C ^
    < content\nother content\ntoms content

In this example we create create a new Grain given two particles, apply an addition grain `tom...` and finally show colloid the result. The `^` caret acts as a directional arrow to assert changes. A shortcut to "the last item".

In this case white-space may be important as `= eric + other` returns the result, however `G =` rather than `G=` may resolve as _agglomerate the two particles then state two grains_ without an operator:

    > G = eric + other
    # Is actually
    < GRAIN(Empty) GRAIN(result)
    # rather than
    > G= eric + other
    < GRAIN(result)

perhaps marking executable steps, like backtick or brackets in classical form:

    > G(eric + other)
    > G<eric + other>
    > G:eric + other:
    > G~eric + other + tom.grain.flooble > C

Expanding this for clarity:

    > GRAIN grain.reference.name AGGLOMERATE particle.reference.name<eric> other.reference.particle<other>
    > GRAIN ^ AGGLOMERATE tom.grain.flooble
    > COLLOID ^
