from typing import Set, List, Dict, Protocol

class Graph:
  def __init__(self, V) -> None:
    self.V = V
    self.adjacency_lists = [[] for i in range(V)]


  def add_edge(self, src, dest):
    self.adjacency_lists[src].append(dest)


  def print_graph(self):
    for i in range(0, self.V, 1):
      print(str(i) + " -> ", end="")
      node = self.adjacency_lists[i]
      for j in range(0, len(node), 1):
        print("{}, ".format(node[j]), end="")
      print("")


  def dfs(self, start):
    visited = [False for i in range(self.V)]
    path = []
    stack = []
    stack.append(start)

    while (len(stack) != 0):
      start = stack.pop()

      if (visited[start] == False):
        path.append(start)
        visited[start] = True

      for node in self.adjacency_lists[start]:
        if (visited[node] == False):
          stack.append(node)

    return path


  def bfs(self, start):
    visited = [False for i in range(self.V)]
    path = []
    queue = []
    queue.append(start)
    visited[start] = True

    while (len(queue) != 0):
      start = queue.pop(0)
      path.append(start)

      for node in self.adjacency_lists[start]:
        if (visited[node] == False):
          queue.append(node)
          visited[node] = True
    return path


g = Graph(13)

g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(1, 7)
g.add_edge(1, 8)
g.add_edge(2, 3)
g.add_edge(2, 6)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(8, 9)
g.add_edge(8, 12)
g.add_edge(9, 10)
g.add_edge(9, 11)

g.print_graph()

dp = g.dfs(0)
bp = g.bfs(0)

print(dp)
print(bp)
