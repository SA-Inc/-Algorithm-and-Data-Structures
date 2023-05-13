# https://leetcode.com/problems/available-captures-for-rook/

def num_rook_captures(board: list[list[str]]) -> int:
  rows = 8
  cols = 8

  rook_row = 0
  rook_col = 0
  captures = 0

  debug = False

  # find Rook Position
  for row in range(0, rows, 1):
    for col in range(0, cols, 1):
      if(board[row][col] == 'R'):
        rook_row = row
        rook_col = col

  if(debug == True): print(rook_row, rook_col)

  # check row right
  for sub_col in range(rook_col + 1, cols, 1):
    if(debug == True): print(board[rook_row][sub_col], rook_row, sub_col)
    if(board[rook_row][sub_col] == 'B'):
      break
    if(board[rook_row][sub_col] == 'p'):
      captures += 1
      break

  # check row left
  for sub_col in range(rook_col - 1, -1, -1):
    if(debug == True): print(board[rook_row][sub_col], rook_row, sub_col)
    if(board[rook_row][sub_col] == 'B'):
      break
    if(board[rook_row][sub_col] == 'p'):
      captures += 1
      break

  # check col down
  for sub_row in range(rook_row + 1, rows, 1):
    if(debug == True): print(board[sub_row][rook_col], sub_row, rook_col)
    if(board[sub_row][rook_col] == 'B'):
      break
    if(board[sub_row][rook_col] == 'p'):
      captures += 1
      break

  # check col up
  for sub_row in range(rook_row - 1, -1, -1):
    if(debug == True): print(board[sub_row][rook_col], sub_row, rook_col)
    if(board[sub_row][rook_col] == 'B'):
      break
    if(board[sub_row][rook_col] == 'p'):
      captures += 1
      break

  return captures


print(num_rook_captures(board = [
  [".",".",".",".",".",".",".","."],
  [".",".",".","p",".",".",".","."],
  [".",".",".","R",".",".",".","p"],
  [".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".","."],
  [".",".",".","p",".",".",".","."],
  [".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".","."]
]))
