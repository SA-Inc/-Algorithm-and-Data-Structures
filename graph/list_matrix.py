def from_adjacency_list_to_adjacency_matrix(adj_list):
  size = len(adj_list)
  adj_matrix = [[0] * size for i in range(size)]

  index = {}
  i = 0

  # keys to index
  for k in adj_list.keys():
    index[k] = i
    i += 1

  for k, v in adj_list.items():
    for i in range(0, len(v), 1):
      # row - from
      # col - to
      adj_matrix[index[k]][index[v[i]]] = 1

  return adj_matrix


def from_adjacency_matrix_to_adjacency_list(adj_matrix):
  d = {}

  for row in range(0, len(adj_matrix), 1):
    d[row] = []
    for col in range(0, len(adj_matrix[row]), 1):
      if(adj_matrix[row][col] == 1):
        d[row].append(col)
      # print(adj_matrix[row][col])

  return d



graph = {
  'A': ['B', 'C'],
  'B': ['A', 'D', 'E'],
  'C': ['A', 'F'],
  'D': ['B'],
  'E': ['B', 'F'],
  'F': ['C', 'E']
}

matrix = [[0, 1, 1, 0, 0, 0], [1, 0, 0, 1, 1, 0], [1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 1, 0]]

# print(from_adjacency_list_to_adjacency_matrix(graph))
print(from_adjacency_matrix_to_adjacency_list(matrix))
