# grid must be square
# primary
# (i == j)
# secondary
# (i + j == n - 1) 

board = [
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]


def primary_diagonals(grid):
  size = len(grid)
  for i in range(0, size, 1):
    print(grid[i][i])

    # control center index (cross)
    if(i != (size - i - 1)):
      pass


def secondary_diagonals(grid):
  size = len(grid)
  for i in range(0, size, 1):
    print(grid[i][size - i - 1])

    # control center index (cross)
    if(i != (size - i - 1)):
      pass


primary_diagonals(board)

secondary_diagonals(board)
