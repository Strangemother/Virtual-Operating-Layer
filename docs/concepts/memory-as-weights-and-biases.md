state: concept

# Neural Network Memory Storage

> Data is linear bits and bytes. What if a "file" of memory is not a static record of bytes, but a neural net of weights and biases, trained to recite the linear data.

The term "data" is a catch-all reference to define structured content. It may be presented as transport data, or storage data - or anything in the ecosystem of IT. And for nearly 80 years digital records of _data_ are verbatim resuscitations of an original article. Some ones voice, a book, or a CSV of finance history - they're all fundamentally the same thing - bits and bytes laid in-sequence, for a LOAD EXECUTE machine to ... load and execute.

Of course we have variation of this _data_. It's compressed, obfuscated, converted to alternative forms to the point where we must identify said _data_ as another product or entity. "This file is not data; it's a zip of photos." or even - it's not bytes, its binary. Never-the-less we can agree upon one absolute - _stored_ data is predominantly procedural bits and bytes in a preferred order.


## Finite States

With the concept of "data" defined we can agree the absolute nature of the _data_ is to persist the _information_ the entity contains albeit to a persistent medium e.g. A storage device, or through transport such as transient data in a network. In all cases the information is relatively _finite_. It has a beginning and and end, it also has _order_ and must be sequenced through a proper EXECUTE statement (consider attempting to view a jpeg in Notepad or Windows Paint).

> Currently in all cases of "data" - it is linear bits - loaded by the correct program

Even with _complex_ structures such as a binary of a ISO or a `.js` scripting file. It's still linear bits and bytes executed correctly by the operating system and an app or two.
It's the same of all information technology today due to modern Von Neumann architecture and its fundamental tenets of STORE LOAD EXECUTE. Additionally the past 15 years has seen a drastic change in the software landscape - where machine learning has gained footing due to better hardware. So currently in all cases, "data" is linear bits and bytes sent to the correct application.

In all cases this record is _finite_ and is expected to start and end. The functionality of the _data_ may change during execution (e.g. an ISO you can run and write into.) but eventually the application will exhaust the records information and release its loading.


## Neural Networks

We enter into the picture - the humble NN or conversationally any clever box of ML tensors of which spit out magic numbers. I generally skirt the topic of ML through my day job as an engineer. I help support the ML team in my company and can generally run a model if the docs are useful.

However I'm the first to say ML  - or more precisely a layered set of interconnected nodes through weights and biases - blows my tiny ape thinker. Personally I find it truly mind blowing a small cluster of fractions in a matrices can resolve such complex answers.

**This is a massive over simplification because ML people know this, non ML don't really care**

---

And to any reader without a cursory knowledge of machine learning - a simple neural net is the porridge of AI. It's no more complex than a few linear equations. There's no need to explain them but the overall idea is silly simple.

Consider a _node_ - it is a number between 0 and 1. It is connected to a list of nodes of the same design. Those second set of nodes will likely connect to an _output_ set of nodes. Each set of these _nodes_ (each being a number between 0 and 1) - are a _layer_. We have three layers - one _in_ one _hidden_ and the _output_. This is upscaled to _as many nodes and layers_ as needed; given some fancy considerations.

And then when we put a number in an input layer; a number pops out in the output layer. It's officially voodoo witchcraft genius.

---

The next question is - how do we _train_ this NN? That's the dark science. Using Math you show this NN everything it should produce; given a certain input.  Eventually the NN will figure out what to say without training data.

^ That's just nuts.


##  Combining Neural Nets and "Data"

Given the assumption we agree on what _data_ is, and a simple NN the concept leads us to the question - is it possible to train a NN upon a dataset, and have it respond with the linear information when _loaded_.

In an example case, we would present a book of Shakespeare to a NN, and it would train to recite it verbatim. The result is a tensor of weights and biases to be transported and read by the receiving program. The receiver loads the Shakespeare model and initiates an _unpack_ of the expected result.

In theory this would reduce any and all "data" into a smaller tensor. If given a compressed version of the original dataset, the result tensor read by the receiver would unpack a zip.

And that it - A neural net representation of a _file_ or dataset. it should _read_ like a file but would not contain the linear bits and bytes and stored content as the NN computes it during the read.


### Considerations

Understandably this is purely conceptual, as the security gaps are bone chilling. But if the result _was_ secure (it could never be without some form of malware detection built into the tensor) we may consider other challenges


### Input Nodes

The dream is minimal input nodes, and one output node announcing bytes for the read stage - however it may be required to provide a count of input nodes, relative to count of bytes within a single input stream.

In other demonstrations for ML based self affirming data structures show _internal compression_ of data entering the NN can reduce the count of hidden nodes. With recursive input nodes reading upon the digest stage during training may could "resuse" neurons through an internal state.

Given the musical box example A internally recurrent signal propagates through the internal nodes until yielding the correct information. Notably the engineer performing the experiment was unaware of the _reason_ for all node actuations during execution. One _unknown node_ seemingly used 4 times during each iteration.


### Building

So 1 input node a larger count of hidden nodes and 1 output node (for a slim dataset) - with the ability to self affirm - a sort of _matricies_ of internal nodes.

I like to think of this as a 3D grid of [9 x 9 x 9] with one input on an edge [node `1`] and an output (node `9`). The hidden grid inside is a self reoccuring NN of sorts.
