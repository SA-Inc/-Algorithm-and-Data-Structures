# https://leetcode.com/problems/largest-local-values-in-a-matrix/

def largest_local(grid: list[list[int]]) -> list[list[int]]:
  grid_size = len(grid)
  local_grid = [[None] * (grid_size - 2) for i in range(grid_size - 2)]

  for row in range(1, grid_size - 1, 1):
    for col in range(1, grid_size - 1, 1):

      local_max = 0

      for sub_row in range(row - 1, row + 2, 1):
        for sub_col in range(col - 1, col + 2, 1):
          if(grid[sub_row][sub_col] > local_max):
            local_max = grid[sub_row][sub_col]

      local_grid[row - 1][col - 1] = local_max

  return local_grid


print(largest_local(grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))
