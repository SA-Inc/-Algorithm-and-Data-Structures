def queens_capture_king(queens: list[list[int]], king: list[int]) -> list[list[int]]:
  def check_left_top(row, col):
    row -= 1
    col -= 1

    while(row >= 0 and col >= 0):
      if(board[row][col] == 'Q'):
        return False
      if(board[row][col] == 'K'):
        # print(row, col)
        return True
      row -= 1
      col -= 1
    return False


  def check_right_top(row, col):
    row -= 1
    col += 1

    while(row >= 0 and col < cols):
      # print(row, col)
      if(board[row][col] == 'Q'):
        return False
      if(board[row][col] == 'K'):
        return True
      row -= 1
      col += 1
    return False


  def check_left_down(row, col):
    row += 1
    col -= 1

    while(row < rows and col >= 0):
      # print(row, col)
      if(board[row][col] == 'Q'):
        return False
      if(board[row][col] == 'K'):
        return True
      row += 1
      col -= 1
    return False


  def check_right_donw(row, col):
    row += 1
    col += 1

    while(row < rows and col < cols):
      # print(row, col)
      if(board[row][col] == 'Q'):
        return False
      if(board[row][col] == 'K'):
        return True
      row += 1
      col += 1
    return False


  def check_left_row(row, col):
    for sub_col in range(col - 1, -1, -1):
      # print(row, sub_col)
      if(board[row][sub_col] == 'Q'):
        return False
      if(board[row][sub_col] == 'K'):
        return True
    return False


  def check_right_row(row, col):
    for sub_col in range(col + 1, cols, 1):
      # print(row, sub_col)
      if(board[row][sub_col] == 'Q'):
        return False
      if(board[row][sub_col] == 'K'):
        return True
    return False


  def check_top_col(row, col):
    for sub_row in range(row - 1, -1, -1):
      # print(sub_row, col)
      if(board[sub_row][col] == 'Q'):
        return False
      if(board[sub_row][col] == 'K'):
        return True
    return False


  def check_down_col(row, col):
    for sub_row in range(row + 1, rows, 1):
      # print(sub_row, col)
      if(board[sub_row][col] == 'Q'):
        return False
      if(board[sub_row][col] == 'K'):
        return True
    return False


  rows = 8
  cols = 8
  result = []
  board = [['_'] * 8 for i in range(8)]

  # place pieces
  board[king[0]][king[1]] = 'K'

  for i in range(0, len(queens), 1):
    queen_row = queens[i][0]
    queen_col = queens[i][1]
    board[queen_row][queen_col] = 'Q'

  for i in range(0, len(board), 1):
    for j in range(0, len(board), 1):
      print(board[i][j], end = ' ')
    print()


  for i in range(0, len(queens), 1):
    queen_row = queens[i][0]
    queen_col = queens[i][1]

    left_row = check_left_row(queen_row, queen_col)
    right_row = check_right_row(queen_row, queen_col)
    top_col = check_top_col(queen_row, queen_col)
    down_col = check_down_col(queen_row, queen_col)
    left_top = check_left_top(queen_row, queen_col)
    right_top = check_right_top(queen_row, queen_col)
    left_down = check_left_down(queen_row, queen_col)
    right_donw = check_right_donw(queen_row, queen_col)

    if(left_row or right_row or top_col or down_col or left_top or right_top or left_down or right_donw):
      result.append([queen_row, queen_col])

  return result


print(queens_capture_king(queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]))
