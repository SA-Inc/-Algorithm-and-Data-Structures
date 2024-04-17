def matrix_sum(matrix_1, matrix_2):
  rows_1 = len(matrix_1)
  cols_1 = len(matrix_1[0])

  rows_2 = len(matrix_2)
  cols_2 = len(matrix_2[0])

  if(rows_1 != rows_2 and cols_1 != cols_2):
    return None

  result = [[0] * cols_1 for i in range(rows_1)]

  for row in range(0, rows_1, 1):
    for col in range(0, cols_1, 1):
      result[row][col] = matrix_1[row][col] + matrix_2[row][col]

  return result
