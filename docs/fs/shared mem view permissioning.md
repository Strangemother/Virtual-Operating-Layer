shared mem view permissioning

1. user writes to the head as 'owner'
2. fetch ref from secret space
3. Use pointer into space
4. yield particle ids for the user


Fast overview:

First the user authenticates the 'header' with the entry username and initial passkey.
This can be anything such as an SSH key. The fs service _accepts_ the message and returns a 'reserved space memory address', initally created by the operating system (the first 0-_n_ reserved read addresses).

The user (reader) service gathers the _key_ from the reserved memory address for future requests. Upon future requests, the user must provide _this_ key to the service.

The given key points to the graphs representing the allowed user content. If the given key does not exist (wrong or new), the addresses will point to a new section of the graph, not the user content.

---


The _file_ access may occur though a function, terminal or socket request. In this example we'll focus on the _terminal_, as this represents the base definition of the vol fs. An initial request will look something like:

    > INITIATE SPACE as {name} with @keyfile
    < 0x123456

This requests the startup _access_ of the space within the service, requested by `{name}` with the initial keyfile. The `{name}` infers a templated variable, likely collected by the local space or user input. The `@keyfile` is a _real file pointer_ to acess some "ready-to-use" data. The name `keyfile` may be any valid name, something the vol fs and OS will understand.

The return value `0x123456` demos a register address within the VOL OS, previously reserved for fs readback, allowing the user to collect the most recent "acces key" - allowing read/write of the user space.

> Consider it like a CSRF token; where the user is expected access to the same shared memory space as the os; this is given through the OS context layer before the user input.

Once the user has this address, they may access the key address to perform read/write. In the OS, another read should access the fs variable:

    ..: userkey=poke(0x123456)
    :.. userkey
    'randomstring'
    ..:


With this we can access the graph:

    > READ 'space.head.user' with @userkey
    < {name}

Starting a read:

    > OPEN @userkey 0/0 foo.bar.baz

Or in a classical functional mode:

    >>> open(filename='foo.bar.baz', position=0/0, key=@userkey)

