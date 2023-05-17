def equal_row_col_pairs(grid: list[list[int]]) -> int:
  rows = len(grid)
  cols = len(grid[0])
  count = 0

  is_row_col = False

  for row in range(0, rows, 1):
    for col in range(0, cols, 1):
      # on each iteration checking set flag on true
      # if elements not equal, set flag to false and check next row/col
      is_row_col = True

      # check adj row and col values
      for i in range(0, rows, 1):
        if(grid[row][i] == grid[i][col]):
          continue
        # if values not equal, skip iteration
        else:
          is_row_col = False
          break

      if(is_row_col == True):
        count += 1

  return count


print(equal_row_col_pairs(grid = [[3,2,1],[1,7,6],[2,7,7]]))
