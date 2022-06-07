# The "Loop"

We refer to the 'loop' a lot as the established runtime executor, however it should be correctly defined as a 'key stepper running at a predicable rate. Once the end of a tree is released is may recycle to a pointer location, or continue to close the 'loop'

When the runtime is established the key pointer moves to the runtime position (likely #0). This executes the BIOD tape statement, building an empty space for any incoming magic key. The initial key should yield _the next key_ pointer to execute, and so on. In baked procedures the stepper doesn't require a pointer return, opting for the next key pointer within a linear index.

As such the 'loop' is more _a walker through a path built for the next step_. The graph may alter, amending the pointer.

---

As the graph exists _away_ from the stepper, many pointers may execute upon one graph. Many unique graphs exist, plugged together through membranes across extra-nets and internal meshes, but they all have a 'pointer' flitting through local intructions.
