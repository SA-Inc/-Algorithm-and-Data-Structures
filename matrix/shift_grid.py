def shift_grid(grid: list[list[int]], k: int) -> list[list[int]]:
  # right shift
  rows = len(grid)
  cols = len(grid[0])

  for _ in range(0, k, 1):
    last = grid[rows - 1][cols - 1]

    # from end to start
    for i in range(rows * cols - 1, -1, -1):
      row = i // cols
      col = i % cols

      prev_row = (i - 1) // cols
      prev_col = (i - 1) % cols

      grid[row][col] = grid[prev_row][prev_col]

    grid[0][0] = last

  return grid


print(shift_grid([[1,2,3],[4,5,6],[7,8,9]], k = 4))
