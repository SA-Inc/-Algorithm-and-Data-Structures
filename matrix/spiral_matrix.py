# looks like two pointers
def spiral_order(matrix):
  rows = len(matrix)
  cols = len(matrix[0])

  # 2d left and right
  row_begin = 0
  row_end = rows - 1
  column_begin = 0
  column_end = cols -1

  result = []

  while(row_begin <= row_end and column_begin <= column_end):
    # move from left to right
    for col in range(column_begin, column_end + 1, 1):
      result.append(matrix[row_begin][col])
    row_begin += 1

    # move from up to down
    for row in range(row_begin, row_end + 1, 1):
      result.append(matrix[row][column_end])
    column_end -=1

    # move from right to left
    if(row_begin <= row_end):
      for col in range(column_end, column_begin - 1, -1):
        result.append(matrix[row_end][col])
    row_end -= 1

    # move from down to up
    if(column_begin <= column_end):
      for row in range(row_end, row_begin - 1, -1):
        result.append(matrix[row][column_begin])
    column_begin += 1

  return result


print(spiral_order(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
