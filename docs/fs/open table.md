# Data Table

An open file has a reference within the graph header space, allocating "open handles" and accessors.

The end user doesn't generally have access to this - unless through exposed iterators. Each reference keeps and maintains the graph pointers for authenticated users.

1. User request file
2. Open Table header
3. Assign counters and readers
4. user accesses fs utils through the assigned header

If no file header exists in the fs allocation table, the file is not "open".
