def matrix_add_sub(m1, m2, addition = True):
  rows_m1 = len(m1)
  cols_m1 = len(m1[0])

  rows_m2 = len(m2)
  cols_m2 = len(m2[0])

  if(rows_m1 != rows_m2 or cols_m1 != cols_m2):
    return -1

  for row in range(0, rows_m1, 1):
    for col in range(0, cols_m1, 1):
      if(addition == True):
        m1[row][col] += m2[row][col]
      else:
        m1[row][col] -= m2[row][col]
  return m1


def transpose(m):
  rows = len(m)
  cols = len(m[0])

  result = [[None] * rows for i in range(cols)]

  for row in range(0, rows, 1):
    for col in range(0, cols, 1):
      result[col][row] = m[row][col]

  return result


def matrix_mul(m, n):
  rows_m = len(m)
  cols_m = len(m[0])

  rows_n = len(n)
  cols_n = len(n[0])

  if(cols_m != rows_n):
    return None

  result = [[None] * cols_n for i in range(rows_m)]

  for row in range(0, rows_m, 1):
    for col in range(0, cols_n, 1):
      result[row][col] = 0

      for i in range(0, rows_n, 1):
        result[row][col] += m[row][i] * n[i][col]

  return result


a = [
  [1, 3],
  [1, 0],
  [1, 2]
]

b = [
  [0, 0],
  [7, 5],
  [2, 1],
]

# print(matrix_add_sub(a, b, False))

print(transpose(a))

print(matrix_mul(transpose(a), b))
