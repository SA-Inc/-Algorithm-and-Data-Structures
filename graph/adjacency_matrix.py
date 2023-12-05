def create_graph(nodes):
  return [[0 for cols in range(nodes)] for rows in range(nodes)]


def add_edge(matrix, src, dst, w):
  matrix[src][dst] = w
  matrix[dst][src] = w


g = create_graph(5)

add_edge(g, 1, 2, 1)
add_edge(g, 3, 0, 2)
add_edge(g, 2, 4, 5)

print(g)
