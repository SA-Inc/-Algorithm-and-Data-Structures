def is_valid_sudoku(board: list[list[int]]) -> bool:
  rows = len(board)
  cols = len(board[0])

  # horizontal
  for row in range(0, rows, 1):
    row_sum = 0

    for col in range(0, cols, 1):
      row_sum += board[row][col]

    if(row_sum != 45):
      return False

  # vertical
  for row in range(0, rows, 1):
    col_sum = 0

    for col in range(0, cols, 1):
      col_sum += board[col][row]

    if(col_sum != 45):
      return False

  # block
  for row in range(0, rows, 3):
    for col in range(0, cols, 3):
      block_sum = 0

      for block_row in range(0, 3, 1):
        for block_col in range(0, 3, 1):
          block_sum += board[row + block_row][col + block_col]

      if(block_sum != 45):
        return False

  return True


print(is_valid_sudoku([
  [5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,8,3,4,2,5,6,7],
  [8,5,9,7,6,1,4,2,3],
  [4,2,6,8,5,3,7,9,1],
  [7,1,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,8,4],
  [2,8,7,4,1,9,6,3,5],
  [3,4,5,2,8,6,1,7,9]
]))
