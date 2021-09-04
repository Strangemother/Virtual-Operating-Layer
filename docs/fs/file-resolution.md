# Resolution

Base methods for resolving an aggregate using grains and pointers don't act like standard files.

Due to chosen build platform the bare-metal communication is done through EXT4 (or the chosen compiler) C libs `seeks`/`read`/`write` bytes. Later this will be changed to a core implmented byte reader, such as ASM  - combining the overall dream of _one memory_ - using a homogeneous space for RAM and _disk_ for resolving in=memory data. In the future magentic disc space will not serve as the main space. With NMVe I can bridge the master-memory with RAM - merging the memory persistence into one giant swap space. At this point it's only useful to use the volatile ram as a security service.


# Pointer Style

The initial design style will incorporate seek based memory swapping for collecting and storing many particles pointers (and content) into RAM. An owning process (and Aggregate) re-reads the store references in RAM, resolving the content for digestion.

An aggregate has one or more grains. Each grain maintains a header and a a local memory reference to particles. All particles resolve to pointer content through personal call procedures.

Each pointer from a particle acts like a single _seek_ style file reference pointer - albeit in-memory, locally persisted, or remote (such as FTP). Upon _seek_ the result content is aggregated by the owner in it's own fashion to result in a complete _file_ for digestion.

Once a pointer seek is exausted it's closed.
