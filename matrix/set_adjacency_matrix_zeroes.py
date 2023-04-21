# https://leetcode.com/problems/set-matrix-zeroes/

def set_zeroes(matrix):
  rows = len(matrix)
  cols = len(matrix[0])
  to_replace = []

  # find cells where perform filling
  for row in range(0, rows, 1):
    for col in range(0, cols, 1):
      if(matrix[row][col] == 0):
        to_replace.append((row, col))

  # filling rows and cols by starting position
  for i in range(0, len(to_replace), 1):
    row = to_replace[i][0]
    col = to_replace[i][1]

    # fill row
    for sub_col in range(0, cols, 1):
      matrix[row][sub_col] = 0

    # fill col
    for sub_row in range(0, rows, 1):
      matrix[sub_row][col] = 0


m = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

set_zeroes(m)

print(m)
