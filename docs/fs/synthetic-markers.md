# Markers and Slicing

At time your may have a very large particle of content and wish to apply additional content somewhere within the data-set. This may occur at the byte level, however for this example we'll consider standard text based content.

We have 50Mb of text and wish to apply an addition 26mb at at marker 30Mb.
This means we move a file pointer to 30Mb of the original file and seek to slice or copy the existing content, finally inserting the addition and stitching the final 20mb.

This is fine and relatively quick, but within a distributed environment this may not be feasable. Considering FTP, a 50mb must be moved. Resulting in 126mb of bandwidth for 26mb of content. Another consideration is a mix of solid and fluid particles. With a solid particle as an injection to an existing peristent store else-where. In the classical case this additional data-structure may only be inserted through forced computation; without leveraging the FS graphing.

# Synthetic marker.

Within a natural dataset such as a large dataset stored remotely, we can apply
markers to iteration points for the fs to consume during iteration. The marker
applys a break point to step into and apply another particle of content to the
content stream. This applys  to the example procedures:

1. multi-pointer threading; opening a classical file on multiple processes and stepping each pointer whilst idle pointers are caching data. When stepping particle spaces, this will speed up late binders.
2. particle stepping: Through many particles within a grain, markers define step points; especially useful with framgmented pointers.
3. Particle Mixture: Inject data updates, encrypted blocks and other late-information to an existing particle.
4. Transient pointer: for pointer replacement for backups or missing code.
