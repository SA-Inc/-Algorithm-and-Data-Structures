# https://leetcode.com/problems/projection-area-of-3d-shapes/

def projection_area(grid: list[list[int]]) -> int:
  rows = len(grid)
  cols = len(grid[0])

  res = 0

  for i in range(0, rows, 1):
    row_max = 0
    col_max = 0

    for j in range(0, cols, 1):
      # X and Y axis
      col_max = max(col_max, grid[i][j])
      row_max = max(row_max, grid[j][i])

      # Z axis
      if(grid[i][j] > 0):
        res += 1

    res += row_max
    res += col_max

  return res
