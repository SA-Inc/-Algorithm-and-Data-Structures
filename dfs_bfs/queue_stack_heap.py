import random
import heapq

rows = 5
cols = 5

matrix = [[0] * cols for _ in range(rows)]

# place random values
for row in range(0, rows, 1):
  for col in range(0, cols, 1):
    matrix[row][col] = random.randint(0, 9)

for row in range(0, rows, 1):
  for col in range(0, cols, 1):
    print(matrix[row][col], end = ' ')
  print()



def dfs(grid, s_row, s_col):
  rows = len(grid)
  cols = len(grid[0])

  d_row = [0, 1, 0, -1]
  d_col = [-1, 0, 1, 0]

  visited = [[False] * cols for _ in range(rows)]
  path = []
  # stack = []
  # queue = []
  heap = []

  # stack.append([s_row, s_col])
  # queue.append([s_row, s_col])
  heapq.heappush(heap, [s_row, s_col])

  # while(len(stack) > 0):
  # while(len(queue) > 0):
  while(len(heap) > 0):
    # top = stack.pop()
    # top = queue.pop(0)
    top = heapq.heappop(heap)
    row = top[0]
    col = top[1]

    if(row < 0 or col < 0 or row >= rows or col >= cols):
      continue
    if(visited[row][col] == True):
      continue

    visited[row][col] = True
    path.append((row, col))

    for i in range(4):
      adj_x = row + d_row[i]
      adj_y = col + d_col[i]
      # stack.append([adj_x, adj_y])
      # queue.append([adj_x, adj_y])
      heapq.heappush(heap, [adj_x, adj_y])

  return path


print(dfs(matrix, 0, 0))
