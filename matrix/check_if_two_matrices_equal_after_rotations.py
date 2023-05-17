def find_rotation(mat: list[list[int]], target: list[list[int]]) -> bool:
  # 2.
  def copmare_matrix(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

    for row in range(0, rows, 1):
      for col in range(0, cols, 1):
        if(matrix1[row][col] != matrix2[row][col]):
          return False

    return True


  # 3.
  def rotate_clockwise(matrix: list[list[int]]):
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(0, rows, 1):
      for col in range(row + 1, cols, 1):
        tmp = matrix[row][col]
        matrix[row][col] = matrix[col][row]
        matrix[col][row] = tmp


    for row in range(0, rows, 1):
      left = 0
      right = rows - 1

      while(left <= right):
        tmp = matrix[row][left]
        matrix[row][left] = matrix[row][right]
        matrix[row][right] = tmp

        left += 1
        right -= 1

    return matrix


  # 1. Rotation by 90 clockwise 3 times
  for _ in range(0, 4, 1):
    if(copmare_matrix(mat, target) == True):
      return True

    mat = rotate_clockwise(mat)

  return False


print(find_rotation(
  mat = [
    [0,0,0],
    [0,1,0],
    [1,1,1]
  ],
  target = [
    [1,1,1],
    [0,1,0],
    [0,0,0]
  ]
))
