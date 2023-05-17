def diagonal_sum(mat: list[list[int]]) -> int:
  n = len(mat)
  d_sum = 0

  # major = [i][i]
  # minor = [i][n - i - 1]

  # sum diagonal at same time
  for i in range(0, n, 1):
    d_sum += mat[i][i]

    if(i != (n - i - 1)):
      d_sum += mat[i][n - i - 1]

  return d_sum


print(diagonal_sum(mat =[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]))
