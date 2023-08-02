# search starts from top right corner (row = 0 and col = n - 1)

def binary_search_matrix(matrix, target):
  row = 0
  col = len(matrix[0]) - 1

  # start from top right position
  while(row < len(matrix) and col >= 0):
    if (matrix[row][col] == target):
      return (row, col)

    if(matrix[row][col] < target):
      row += 1
    else:
      col -= 1

  return (-1, -1)


m = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
]

print(binary_search_matrix(m, 7))
