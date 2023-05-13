def island_perimeter(grid: list[list[int]]) -> int:
  rows = len(grid)
  cols = len(grid[0])
  perimeter = 0

  for row in range(0, rows, 1):
    for col in range(0, cols, 1):
      if(grid[row][col] == 1):
        # add all sides and then remove if needed
        perimeter += 4

        # check sides and bounds
        # if value is 1 on adjacency side cell, minus 1
        # else minus 0
        # (check bound and minus neighbor value)

        # up
        if(row > 0):
          perimeter -= grid[row - 1][col]

        # down
        if(row < rows - 1):
          perimeter -= grid[row + 1][col]

        # left
        if(col > 0):
          perimeter -= grid[row][col - 1]

        # right
        if(col < cols - 1):
          perimeter -= grid[row][col + 1]

  return perimeter


print(island_perimeter(grid = [
  [0,1,0,0],
  [1,1,1,0],
  [0,1,0,0],
  [1,1,0,0]
]))
