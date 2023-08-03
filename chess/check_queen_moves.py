rows = 8
cols = 8
board = [['_'] * 8 for i in range(8)]

queen = (3, 2)


def check_left_top(row, col):
  row -= 1
  col -= 1

  while(row >= 0 and col >= 0):
    print(row, col)
    row -= 1
    col -= 1


def check_right_top(row, col):
  row -= 1
  col += 1

  while(row >= 0 and col < cols):
    print(row, col)
    row -= 1
    col += 1


def check_left_down(row, col):
  row += 1
  col -= 1

  while(row < rows and col >= 0):
    print(row, col)
    row += 1
    col -= 1


def check_right_donw(row, col):
  row += 1
  col += 1

  while(row < rows and col < cols):
    print(row, col)
    row += 1
    col += 1


def check_left_row(row, col):
  for sub_col in range(col - 1, -1, -1):
    print(row, sub_col)


def check_right_row(row, col):
  for sub_col in range(col + 1, cols, 1):
    print(row, sub_col)


def check_top_col(row, col):
  for sub_row in range(row - 1, -1, -1):
    print(sub_row, col)


def check_down_col(row, col):
  for sub_row in range(row + 1, rows, 1):
    print(sub_row, col)



check_left_row(queen[0], queen[1])
# check_right_row(queen[0], queen[1])
# check_top_col(queen[0], queen[1])
# check_down_col(queen[0], queen[1])
# check_left_top(queen[0], queen[1])
# check_right_top(queen[0], queen[1])
# check_left_down(queen[0], queen[1])
# check_right_donw(queen[0], queen[1])
