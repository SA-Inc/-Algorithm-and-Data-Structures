def count_squares(matrix: list[list[int]]) -> int:
  # count squares with all filled ones
  rows = len(matrix)
  cols = len(matrix[0])

  squares = 0

  # loop
  for row in range(1, rows, 1):
    for col in range(1, cols, 1):
      # formula
      if(matrix[row][col] == 0):
        continue

      # each cell contain square size
      matrix[row][col] = min([matrix[row - 1][col], matrix[row][col - 1], matrix[row - 1][col - 1]]) + 1

  for row in range(0, rows, 1):
    for col in range(0, cols, 1):
      squares += matrix[row][col]

  return squares


print(count_squares(matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]))
