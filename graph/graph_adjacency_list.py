class Graph:
    # Directed Weighted Graph
    def __init__(self, name = 'New Graph'):
        self.name = name
        self.nodes = []
        self.edges = {}

    def addNode(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
            return True
        else:
            return False

    def addEdge(self, nodeFrom, nodeTo, weight):
        tmp = []
        if nodeFrom in self.nodes and nodeTo in self.nodes:
            if nodeFrom not in self.edges:
                tmp.append((nodeTo, weight))
                self.edges[nodeFrom] = tmp
            elif nodeFrom in self.edges:
                tmp.extend(self.edges[nodeFrom]) 
                tmp.append((nodeTo, weight))
                self.edges[nodeFrom] = tmp
            return True
        else:
            return False

    def bfs(self, startNode):
        visited = []
        queue = []

        visited.append(startNode)
        queue.append(startNode)

        # while len(queue) != 0:
        while queue:
            currentNode = queue.pop(0)
            if currentNode in self.edges:
                for neighbour in self.edges[currentNode]:
                    if neighbour[0] not in visited:
                        visited.append(neighbour[0])
                        queue.append(neighbour[0])

        return visited

    def dfs(self, startNode):
        visited = []
        stack = []

        stack.append(startNode)

        while stack:
            currentNode = stack.pop()

            if currentNode in visited:
                continue
            visited.append(currentNode)

            if currentNode in self.edges:
                for neighbour in self.edges[currentNode]:
                    stack.append(neighbour[0])

        return visited

    # def dijkstra(self, nodeFrom, nodeTo):
    #     distance = {}
    #     queue = []

    #     for node in self.nodes:
    #         distance[node] = 999999999999
    #         queue.append(node)

    #     distance[nodeFrom] = 0

    #     while queue:


    #     # return 

    def printGraph(self):
        for node in self.edges:
            print("{} -> {}".format(node, [i for i in self.edges[node]]))

g = Graph()

#Adding nodes
g.addNode(0)
g.addNode(1)
g.addNode(2)
g.addNode(3)
g.addNode(4)

g.addNode(5)
g.addNode(6)
g.addNode(7)
g.addNode(8)
g.addNode(9)
g.addNode(10)
g.addNode(11)
g.addNode(12)
g.addNode(13)
g.addNode(14)
g.addNode(15)

#Adding edges
g.addEdge(0, 1, 2)
g.addEdge(1, 2, 2)
g.addEdge(2, 3, 4)
g.addEdge(3, 0, 5)
g.addEdge(3, 4, 3)
g.addEdge(4, 0, 1)

g.addEdge(0, 5, 1)
g.addEdge(0, 6, 7)
g.addEdge(7, 0, 5)
g.addEdge(2, 8, 3)
g.addEdge(8, 10, 4)
g.addEdge(3, 9, 5)
g.addEdge(8, 10, 4)
g.addEdge(10, 11, 4)
g.addEdge(11, 12, 5)
g.addEdge(4, 13, 5)
g.addEdge(13, 14, 5)
g.addEdge(14, 15, 5)

g.addEdge(6, 12, 7)
g.addEdge(5, 12, 12)
 
#Printing the graph
g.printGraph()

print('BFS', g.bfs(0))
print('DFS', g.dfs(0))
# print(g.dijkstra(0, 12))
