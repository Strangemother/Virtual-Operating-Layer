# Simple Graph

The above code provides a simple implementation of a graph data structure in Nim. It allows you to create nodes and edges, and perform basic requests for nodes.

1. add node to node 
2. add edge to node
3. remove node from graph
4. remove edge from node

This is a stateless service, meaning that it does not maintain any state between requests. Each request is independent and does not rely on any previous requests.

## Usage

the `flatgraph` provides minimal functionality.

```nim
flatgraph.connect("A", "B") # Connects node A to node B
flatgraph.connect("C", "B") # Connects node C to node B

flatgraph.from("A") # returns ["B"]
flatgraph.to("B") # returns ["A", "C"]

flatgraph.remove("A", "B") # removes the edge from node A to node B
```

