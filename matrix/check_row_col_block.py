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


def check_row(board, row):
  cols = len(board[0])
  for sub_col in range(0, cols, 1):
    print(board[row][sub_col])


def check_col(board, col):
  rows = len(board)
  for sub_row in range(0, rows, 1):
    print(board[sub_row][col])


# check block (from top-right to size, not middle)
def check_block(board, row, col, size):
  rows = len(board)
  cols = len(board[0])

  row_block_start = size * (row // size)
  col_block_start = size * (col // size)
  row_block_end = row_block_start + size
  col_block_end = col_block_start + size

  for block_row in range(row_block_start, row_block_end, 1):
    for block_col in range(col_block_start, col_block_end, 1):
      print(board[block_row][block_col])


def check_row_skip_start(board, row):
  cols = len(board[0])
  for sub_col in range(0, cols, 1):
    if(row != sub_col):
      print(board[row][sub_col])


def check_col_skip_start(board, col):
  rows = len(board)
  for sub_row in range(0, rows, 1):
    if(col != sub_row):
      print(board[sub_row][col])

check_row(board, 1)

check_col(board, 1)

check_block(board, 3, 3, 2)

check_row_skip_start(board, 1)

check_col_skip_start(board, 1)
