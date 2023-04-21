# init matrix and new matrix must be same size

def matrix_reshape(matrix, result_rows, result_cols):
  rows = len(matrix)
  cols = len(matrix[0])

  if(rows * cols != result_rows * result_cols):
    return matrix

  temp_array = []
  new_matrix = []

  # 2d array to temp 1d array
  for i in range(0, rows * cols, 1):
    row = i // cols
    col = i % cols
    temp_array.append(matrix[row][col])

  # 1d array to new 2d array
  for row in range(0, result_rows, 1):
    temp_row = []
    for col in range(0, result_cols, 1):
      temp_row.append(temp_array[row * result_cols + col])
    new_matrix.append(temp_row)

  return new_matrix


print(matrix_reshape([[1,2],[3,4]], 1, 4))
