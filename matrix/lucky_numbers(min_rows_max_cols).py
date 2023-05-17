def lucky_numbers(matrix: list[list[int]]) -> list[int]:
  rows = len(matrix)
  cols = len(matrix[0])

  result = []
  min_in_rows = [100000] * rows
  max_in_cols = [0] * cols

  # save min on each rows and max on each cols
  for row in range(0, rows, 1):
    for col in range(0, cols, 1):
      min_in_rows[row] = min(min_in_rows[row], matrix[row][col])
      max_in_cols[col] = max(max_in_cols[col], matrix[row][col])

  # if values on each arrays are equal (crossing) append to result
  for row in range(0, rows, 1):
    for col in range(0, cols, 1):
      if(min_in_rows[row] == max_in_cols[col]):
        result.append(min_in_rows[row])

  # print(min_in_rows)
  # print(max_in_cols)

  return result


print(lucky_numbers(matrix = [[3,7,8],[9,11,13],[15,16,17]]))
