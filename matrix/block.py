# naive approach (4 inner loops)
# and block size must be multiple of rows and cols
# (ex. 9 row/col size => 3 block size)

def sudoku_block(board):
  rows = len(board)
  cols = len(board[0])
  block_size = 3
  for row in range(0, rows, block_size):
    for col in range(0, cols, block_size):
      for block_row in range(0, block_size, 1):
        for block_col in range(0, block_size, 1):
          print(board[row + block_row][col + block_col])
      print()


# more advanced variant (round position) and custom square size
def block(board, row, col, size):
  row_block_start = size * (row // size)
  col_block_start = size * (col // size)
  row_block_end = row_block_start + size
  col_block_end = col_block_start + size

  for block_row in range(row_block_start, row_block_end, 1):
    for block_col in range(col_block_start, col_block_end, 1):
      print(board[block_row][block_col])


board = [
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

block(board, 2, 1, 4)
