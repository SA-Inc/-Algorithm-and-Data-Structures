def word_search(board: list[list[str]], word: str) -> bool:
  def dfs_search_word_iterative(grid, s_row, s_col, word):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)] # left, down, right, up

    stack = []
    visited = set()
    word_index = 0

    stack.append((s_row, s_col, word_index, False))

    while(len(stack) > 0):
      top = stack.pop()
      row = top[0]
      col = top[1]
      i = top[2]
      is_backtrack = top[3]

      if(is_backtrack == True):
        visited.remove((row, col))
        continue

      visited.add((row, col))
      stack.append((row, col, i, True))

      if(i == len(word) - 1):
        return True

      for d in range(4):
        adj_row = row + directions[d][0]
        adj_col = col + directions[d][1]

        if(row < 0 and col < 0 and row >= rows and col >= cols):
          if((adj_row, adj_col) in visited):
            continue
          if(grid[adj_row][adj_col] == word[i + 1]):
            stack.append([adj_row, adj_col, i + 1, False])

    return True


  rows = len(board)
  cols = len(board[0])

  for row in range(0, rows, 1):
    for col in range(0, cols, 1):
      if(board[row][col] == word[0]):
        is_found = dfs_search_word_iterative(board, row, col, word)

        if(is_found == True):
          return True

  return False
