a = [
  [2, 3, 1],
  [5, 7, 3],
  [9, 1, 0],
  [2, 4, 2]
]


def sum_by_row(array):
  sums = []
  rows = len(array)
  cols = len(array[0])

  for row in range(0, rows, 1):
    row_sum = 0
    for col in range(0, cols, 1):
      row_sum += array[row][col]
    sums.append(row_sum)
  return sums


def sum_by_col(array):
  sums = []
  rows = len(array)
  cols = len(array[0])

  for col in range(0, cols, 1):
    col_sum = 0
    for row in range(0, rows, 1):
      col_sum += array[row][col]
    sums.append(col_sum)
  return sums


print(sum_by_row(a))

print(sum_by_col(a))
