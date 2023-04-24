def matrix_score(grid):
  def flip_row(grid, row):
    for col in range(0, cols, 1):
      grid[row][col] ^= 1

  def flip_col(grid, col):
    for row in range(0, rows, 1):
      grid[row][col] ^= 1

  def bin_array_to_number(arr):
    number = 0
    for digit in arr:
      number = (number << 1) | digit
    return number

  rows = len(grid)
  cols = len(grid[0])
  result = 0

  # if MSB == 1 skip, because alredy large num, else, flip number
  for row in range(0, rows, 1):
    if(grid[row][0] == 0):
      flip_row(grid, row)

  transposed = list(zip(*grid))

  for col in range(0, cols, 1):
    if(grid[0][col] == 0):
      flip_col(grid, col)
      # print(transposed[col][0])

  for row in range(0, rows, 1):
    result += bin_array_to_number(grid[row])

  return result
