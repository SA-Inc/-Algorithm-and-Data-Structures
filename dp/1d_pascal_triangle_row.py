def pascal_triangle_get_row(row_index: int) -> list[int]:
  result = []
  row = []

  for i in range(0, row_index + 1, 1):
    row = [1] + row

    for j in range(1, len(row) - 1, 1):
      row[j] += row[j + 1]

    result.append(row)

  return result[row_index]


print(pascal_triangle_get_row(3))
