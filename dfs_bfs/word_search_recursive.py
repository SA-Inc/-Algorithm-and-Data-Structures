def word_search(board: list[list[str]], word: str) -> bool:
  def dfs_search_word_recursive(grid, row, col, word, index):
    # base case, end recursion
    if(index == len(word)):
      return True

    # out of bound or visited or not matched
    if(row < 0 or col < 0 or row >= rows or col >= cols or word[index] != grid[row][col]):
      return False

    # visited
    grid[row][col] = '*'

    result = dfs_search_word_recursive(grid, row - 1, col, word, index + 1) or dfs_search_word_recursive(grid, row + 1, col, word, index + 1) or dfs_search_word_recursive(grid, row, col - 1, word, index + 1) or dfs_search_word_recursive(grid, row, col + 1, word, index + 1)
    grid[row][col] = word[index]
    return result


  rows = len(board)
  cols = len(board[0])

  for row in range(0, rows, 1):
    for col in range(0, cols, 1):
      if(board[row][col] == word[0]):
        is_found = dfs_search_word_recursive(board, row, col, word, 0)

        if(is_found == True):
          return True

  return False
