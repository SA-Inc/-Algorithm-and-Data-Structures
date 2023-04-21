image = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]


# work only with squared images
# by 90 clockwise
# 1. transpose matrix
# 2. reverse rows
def rotate(matrix):
  rows = len(matrix)
  cols = len(matrix[0])

  # transpose
  for row in range(0, rows, 1):
    for col in range(row + 1, cols, 1):
      tmp = matrix[row][col]
      matrix[row][col] = matrix[col][row]
      matrix[col][row] = tmp

  # reverse
  for row in range(0, rows, 1):
    left = 0
    right = rows - 1

    while(left <= right):
      tmp = matrix[row][left]
      matrix[row][left] = matrix[row][right]
      matrix[row][right] = tmp

      left += 1
      right -= 1


rotate(image)

print(image)
