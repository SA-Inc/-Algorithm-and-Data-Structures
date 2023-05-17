def diagonal_sort(mat: list[list[int]]) -> list[list[int]]:
  rows = len(mat)
  cols = len(mat[0])

  d = {}

  # save diagonals (real and virtual)
  for row in range(0, rows, 1):
    for col in range(0, cols, 1):
      if(row - col in d):
        d[row - col].append(mat[row][col])
      else:
        d[row - col] = []
        d[row - col].append(mat[row][col])

  # sort each diagonal
  for key in d:
    d[key].sort(reverse = True)

  # restore sorted
  for row in range(0, rows, 1):
    for col in range(0, cols, 1):
      mat[row][col] = d[row - col].pop()

  return mat


print(diagonal_sort(mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
