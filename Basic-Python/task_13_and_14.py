from queue import Queue

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
            print('error m8')

    def addEdge(self, nodeOne, nodeTwo):
        self.vertices.get(nodeOne).adjacent.append(nodeTwo)
        self.vertices.get(nodeTwo).adjacent.append(nodeOne)


    def DFS(self, start_node):
        stack = []
        visited = []
        stack.append(start_node)

        while len(stack) > 0:
            u = stack.pop()
            if u not in visited:
                for e in graph.vertices[u].adjacent:
                    stack.append(e)
                visited.append(u)

        print(visited)

    def BFS(self, start_node):
        q = Queue()
        visited = []
        q.put(start_node)
        while q.qsize() > 0:
            u = q.get()
            if u not in visited:
                for e in self.vertices[u].adjacent:
                    q.put(e)
                visited.append(u)

        print(visited)

if __name__ == "__main__":

    graph = Graph()

    graph.addNode("A")
    graph.addNode("B")
    graph.addNode("C")
    graph.addNode("D")
    graph.addNode("E")

    graph.addEdge("A", "B")
    graph.addEdge("B", "D")
    graph.addEdge("C", "D")
    graph.addEdge("C", "E")
    graph.addEdge("D", "E")

    graph.DFS("C")
    graph.BFS("C")


    # print(graph.vertices.get("C").adjacent)