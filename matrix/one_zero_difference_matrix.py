# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

def ones_minus_zeros(grid: list[list[int]]) -> list[list[int]]:
  rows = len(grid)
  cols = len(grid[0])

  row_ones = [0] * rows
  col_ones = [0] * cols
  diff = [[None] * cols for i in range(rows)]

  # count ones in rows and cols
  for row in range(0, rows, 1):
    for col in range(0, cols, 1):
      if(grid[row][col] == 1):
        row_ones[row] += 1
        col_ones[col] += 1

  # fill new matrix by formula
  for row in range(0, rows, 1):
    for col in range(0, cols, 1):
      # diff[row][col] = row_ones + col_ones - row_zeros - col_zeros
      diff[row][col] = row_ones[row] + col_ones[col] - (rows - row_ones[row]) - (cols - col_ones[col])

  return diff


print(ones_minus_zeros(grid = [[0,1,1],[1,0,1],[0,0,1]]))
