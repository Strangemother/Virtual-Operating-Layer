# Key graph with a stepping graph


A list of words have the potential to yield.

         positions
    --------------------
    #   0 1 2 3 4 5    i
    --------------------
    0   A P P L E S    0
    1   B A N A N A    1
    2   W I N D O W    1
    3   W I N D Y      1
    4   H E L L O      3
    5   H E L P        3
    6   H E A D S      3


Per each input the _terminal char_ is incremented or dropped. In the above example `HE` moves postion #5, #6, and #7 to index `2`. If the next input char yields `L` or `A` the term continues.

`i` is a positive int, thus starting at postition `1` (not zero), any identified `0` keys are assigned _unused_, and all failed keys index from `1`. Any subsequent test becomes

    positions[i-1]

for the identified key position, with `positions[i]` as the _expected incoming potential_.

To reduce the cost of testing for strings, each postion has a key graph, connecting to indexes of siblings. The identity of the graph is the left right position with keys of the graph being the letters of that column.

Graph #3 (column 2) looks something like:

\#3:

    P > L
    L > L | P
    A > D
    N > A | D

for wholness graph #4 (column 3) looks like:

\#4:

    L > E | O
    A > N
    D > O | Y | D
    P

As such when executing a key graph step, it's a case of verfiying if the `i` equals the length of the given matches.

----

When in-use, each referer has this table reference - similar to `tell` and `seek` in classical pipes. Key positions store against the row index, graph positions and `i` terminal index. The above table is stored as a sparse index:

    #4 3
    #5 3
    #6 3

For less complex repeats, the transation placement may simply be retested with the reference `HE`.
