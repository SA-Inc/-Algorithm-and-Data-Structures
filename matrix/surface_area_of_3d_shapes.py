def surface_area(grid: list[list[int]]) -> int:
  # all 6 sides and inner possible voids
  rows = len(grid)
  cols = len(grid[0])
  row_dir = [0, 1, 0, -1]
  col_dir = [1, 0, -1, 0]

  res = 0

  for row in range(0, rows, 1):
    for col in range(0, cols, 1):
      # up and bottom sides
      if(grid[row][col] > 0):
        res += 2

        # west, north, east, south sides
        for side in range(0, 4, 1):
          neighbor_row = row + row_dir[side]
          neighbor_col = col + col_dir[side]
          neighbor_value = 0

          # check out of bounds
          if(0 <= neighbor_row and neighbor_row < rows and 0 <= neighbor_col and neighbor_col < cols):
            neighbor_value = grid[neighbor_row][neighbor_col]

          res += max(grid[row][col] - neighbor_value, 0)

  return res
