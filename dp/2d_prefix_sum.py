def prefix_sum(mat):
  rows = len(mat)
  cols = len(mat[0])
  dp = [[0] * cols for i in range(rows)]

  # fill 1st row
  for col in range(0, cols, 1):
    dp[0][col] = dp[0][col - 1] + mat[0][col]
  # fill 1st col
  for row in range(0, rows, 1):
    dp[row][0] = dp[row - 1][0] + mat[row][0]

  for row in range(1, rows, 1):
    for col in range(1, cols, 1):
      dp[row][col] = dp[row - 1][col] + dp[row][col - 1] - dp[row - 1][col - 1] + mat[row][col]

  return dp


print(prefix_sum([
  [1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1],
]))
