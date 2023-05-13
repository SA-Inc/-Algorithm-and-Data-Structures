# https://leetcode.com/problems/max-increase-to-keep-city-skyline/

def transpose(grid, rows, cols):
  for row in range(0, rows, 1):
    for col in range(row + 1, cols, 1):
      tmp = grid[row][col]
      grid[row][col] = grid[col][row]
      grid[col][row] = tmp

def max_increase_keeping_skyline(grid: list[list[int]]) -> int:
  rows = len(grid)
  cols = len(grid[0])

  max_rows = [None] * rows
  max_cols = [None] * cols
  total_sum = 0

  for row in range(0, rows, 1):
    max_rows[row] = max(grid[row])

  transpose(grid, rows, cols)

  for col in range(0, cols, 1):
    max_cols[col] = max(grid[col])

  transpose(grid, rows, cols)

  for row in range(0, rows, 1):
    for col in range(0, cols, 1):
      min_height = min(max_rows[row], max_cols[col])
      total_sum += abs(grid[row][col] - min_height)
      grid[row][col] = min_height

  return total_sum


print(max_increase_keeping_skyline(grid = [
  [3,0,8,4],
  [2,4,5,7],
  [9,2,6,3],
  [0,3,1,0]
]))
