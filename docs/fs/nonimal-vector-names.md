# Vector Naming

Key Value vectors, or nominal vectors are names asssociated with files to utilise storage locations through arbitrary particle definitions.

Consider Vector names liek tagging, but with specific locations designated to each key. By design the system will leverage a tri-state vector - or three key locale. Providing a three key local as a name to the particle, the system will create, define and manage the a vector address as a table. Utilising three tables (or more) we can derive:

+ Shorter and long key search (with faster needle aggrgation)
+ data distributation through naming; "element.audio.remote" for example

---

We'll focus on three-state vectors, but more can be applied without change. A particle (or a 'file' consisting of many chunks; a particle being one chunk) defines an address and content. The particle content is stored anywhere in the FS membrane and the address is held by header or phenocryst for later gathers into grains and aggregates.

A particle address is given back from the write store when the content is persistently confirmed. The address may be one of many, to apply under the general particle "name" - a tree-vector.

The three vector names may be anything; notable a user will pick three familiar words, gathers a silent key store of the assigned words. A particle name may be unique or shared. A paricle address is always unique.

Therefore a call to fetch a paticle by name will always yield a list of one or more. Each content from the addresses is merged for a grain.


# Space names

And area or space may activate through its vector named - to utilised by the named particle. The example vector name:

    audio.eric.wedding

defines three nonimal spaces. Each with their own procedures. The 'audio' space may expectantly handle pull/push to a store location for audio only. With soft-space definitions a user may define a standar index against 'wedding' _however the system may generate one anyway_.

define a unique subsection of the space with a key assignment:

    audio.eric.wedding:main-morning-speech

For a local reference a friendly name expands this vector name for humans. Only one unique sort-name may exist.

    my-morning-speech -> audio.eric.wedding:main-morning-speech

For common particles, bake the space addresses to the local index to crystalise the phenocryst. This has advantages of speed-up throughput, but will yield errors if the particle addresses bind to transient spaces.
