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


# normal loop
def row_major_order(board):
  rows = len(board)
  cols = len(board[0])
  for row in range(0, rows, 1):
    for col in range(0, cols, 1):
      print(board[row][col], end=' ')
    print()


# transposed loop
def col_major_order(board):
  rows = len(board)
  cols = len(board[0])
  for row in range(0, rows, 1):
    for col in range(0, cols, 1):
      print(board[col][row], end=' ')
    print()


row_major_order(board)

col_major_order(board)
