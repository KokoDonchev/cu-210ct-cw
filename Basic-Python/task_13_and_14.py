"""
Week 7 Task 1 and Task 2

Write the pseudocode for an unweighted graph data structure. You either use an
adjacency matrix or an adjacency list approach. Also, write a function to add
a new node and a function to add an edge. Following that, implement the graph
you have designed in the programming language of your choice. You may use your
own linked list from previous labs, the STL LL, or use a simple fixed size array
(10 elements would be fine).

Implement BFS and DFS traversals for the above graph. Save the nodes
traversed in sequence to a text file.

Pseudocode

CLASS VERTEX
    init(label)
        label <- label
        adjacent <- []

CLASS GRAPH
    init()
        vertices <- new Dict()

    ADD-NODE(label)
        IF label is not in vertices
            vertices[label] = VERTEX(label)
        ELSE
            return Error

    ADD-EDGE(node1, node2)
        vertices[node1].adjacent.push(node2)
        vertices[node2].adjacent.push(node1)

"""

class Vertex(object):

    def __init__(self, label):
        self.label = label
        self.adjacent = []

class Graph(object):

    def __init__(self):
        self.vertices = {}

    def addNode(self, label):
        if label not in self.vertices:
            self.vertices[label] = Vertex(label)
        else:
            print('Error: A node with label %s already exists!' % label)

    def addEdge(self, nodeOne, nodeTwo):
        self.vertices.get(nodeOne).adjacent.append(nodeTwo)
        self.vertices.get(nodeTwo).adjacent.append(nodeOne)


    def DFS(self, v):
        stack = []
        visited = []
        stack.append(v)

        while len(stack) > 0:
            u = stack.pop()
            if u not in visited:
                for e in graph.vertices[u].adjacent:
                    stack.append(e)
                visited.append(u)
        file = open("DFS-result.txt", "w")
        file.write(str(visited))
        file.close()

    def BFS(self, v):
        q = []
        visited = []
        q.append(v)

        while len(q) > 0:
            u = q.pop(0)
            if u not in visited:
                for e in self.vertices[u].adjacent:
                    q.append(e)
                visited.append(u)
        file = open("BFS-result.txt", "w")
        file.write(str(visited))
        file.close()

if __name__ == "__main__":

    graph = Graph()

    graph.addNode("A")
    graph.addNode("B")
    graph.addNode("C")
    graph.addNode("D")
    graph.addNode("E")
    graph.addNode("F")
    graph.addNode("G")
    graph.addNode("H")
    graph.addNode("I")

    graph.addEdge("A", "B")
    graph.addEdge("B", "D")
    graph.addEdge("C", "D")
    graph.addEdge("C", "A")
    graph.addEdge("D", "C")
    graph.addEdge("G", "H")
    graph.addEdge("I", "A")
    graph.addEdge("H", "I")

    graph.DFS("C")
    graph.BFS("C")


    # print(graph.vertices.get("C").adjacent)