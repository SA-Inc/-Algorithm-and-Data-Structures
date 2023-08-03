a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rows = 2
cols = 5


def row_major_matrix(array, rows, cols):
  for row in range(0, rows, 1):
    for col in range(0, cols, 1):
      print('row = {} col = {}: {}'.format(row, col, array[row * cols + col]))

def row_major_matrix_red(array, cols, index):
  for index in range(0, len(array), 1):
    col = index % cols
    row = (index - col) // cols
    print('row = {} col = {}: {}'.format(row, col, array[index]))


def col_major_matrix(array, rows, cols):
  for col in range(0, cols, 1):
    for row in range(0, rows, 1):
      print('row = {} col = {}: {}'.format(row, col, array[col * rows + row]))

def col_major_matrix_red(array, rows, index):
  for index in range(0, len(array), 1):
    row = index % rows
    col = (index - row) // rows
    print('row = {} col = {}: {}'.format(row, col, array[index]))


row_major_matrix(a, rows, cols)
row_major_matrix_red(a, rows, cols)
col_major_matrix(a, rows, cols)
col_major_matrix_red(a, rows, cols)
