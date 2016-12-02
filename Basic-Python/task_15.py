"""
Week 8 Task 1

Implement Dijkstra’s algorithm for a weighted graph data structure (you have
to update your previous data structure so that it can deal with weights).

"""

class Vertex(object):

    def __init__(self, label):
        self.label = label
        self.adjacents = {} # this time dict because of the new values
        self.tw = float('inf') # we set the tentative weight to infinity
        self.pre = None # previous node

class Graph(object):

    def __init__(self):
        self.vertices = {}

    def addNode(self, label):
        if label not in self.vertices:
            self.vertices[label] = Vertex(label)
        else:
            print('Error: A node with label %s already exists!' % label)

    def addEdge(self, nodeOne, nodeTwo, weight):
        self.vertices.get(nodeOne).adjacents[nodeTwo] = weight
        self.vertices.get(nodeTwo).adjacents[nodeOne] = weight

    def Dijkstra(self, s, d): # s - source / d - destination
        """
        The whole Dijkstra algorithm is based on the example from
        our lectures
        """
        s = self.vertices[s]
        d = self.vertices[d]

        v = s # currently scanned node
        s.tw = 0
        visited = []
        while v != d:
            for u in v.adjacents.keys():  # adjacent vertices from current one
                u = self.vertices[u]
                if v.tw + u.adjacents[v.label] < u.tw:
                    u.tw = v.tw + u.adjacents[v.label]
                    u.pre = v

            visited.append(v)

            min = float('inf')

            for i in self.vertices.values():
                if i not in visited and i.tw < min:
                    v = i
                    min = i.tw

        return v.tw

if __name__ == '__main__':

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


    graph.addEdge("A", "G", 5)
    graph.addEdge("E", "G", 5)
    graph.addEdge("E", "C", 3)
    graph.addEdge("G", "F", 8)
    graph.addEdge("G", "C", 16)
    graph.addEdge("G", "E", 4)
    graph.addEdge("A", "B", 3)
    graph.addEdge("C", "F", 0)
    graph.addEdge("C", "I", 4)
    graph.addEdge("C", "H", 5)


    print(graph.Dijkstra("A", "C"))
    print('Vertices:', graph.vertices)
    print('A edges: ', graph.vertices.get("A").adjacents)
    print('C edges: ',graph.vertices.get("C").adjacents)