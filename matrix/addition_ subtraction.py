def matrix_add(m1, m2, addition = True):
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

print(matrix_add(a, b, False))
