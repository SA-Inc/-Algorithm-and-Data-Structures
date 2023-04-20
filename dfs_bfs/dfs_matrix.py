def dfs(matrix, rows, cols, start):
  # up, right, down, left
  directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
  stack = []
  visited = [[False] * cols for _ in range(rows)]

  start_row = start[0]
  start_col = start[1]
  stack.append((start_row, start_col))
  visited[start_row][start_col] = True

  while(len(stack) > 0):
    top = stack.pop()
    row = top[0]
    col = top[1]

    # perform our actions
    print(row, col, matrix[row][col])

    # add adjacency cells
    for i in range(4):
      adj_x = row + directions[i][0]
      adj_y = col + directions[i][1]

      # check out of bounds
      if(adj_x >= 0 and adj_y >= 0 and adj_x < rows and adj_y < cols and visited[adj_x][adj_y] != True):
        # mark as visited
        visited[adj_x][adj_y] = True
        stack.append((adj_x, adj_y))


m = [
  [1, 2, 3, 4, 5, 6],
  [7, 8, 9, 10, 11, 12],
  [13, 14, 15, 16, 17, 18],
  [19, 20, 21, 22, 23, 24],
  [25, 26, 27, 28, 29, 30],
  [31, 32, 33, 34, 35, 36],
]

rows = len(m)
cols = len(m[0])

dfs(m, rows, cols, (0, 0))
