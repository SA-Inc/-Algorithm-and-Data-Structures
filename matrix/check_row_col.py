def check_row(board, row):
  cols = len(board[0])
  for sub_col in range(0, cols, 1):
    print(board[row][sub_col])


def check_col(board, col):
  rows = len(board)
  for sub_row in range(0, rows, 1):
    print(board[sub_row][col])


check_row(board, 1)

check_col(board, 1)
