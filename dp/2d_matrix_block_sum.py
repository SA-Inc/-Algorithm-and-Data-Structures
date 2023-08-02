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


def matrix_block_sum(mat: list[list[int]], k: int) -> list[list[int]]:
  rows = len(mat)
  cols = len(mat[0])
  result = [[0] * cols for i in range(rows)]
  dp = prefix_sum(mat)

  for row in range(0, rows, 1):
    for col in range(0, cols, 1):
      min_row = max(0, row - k)
      min_col = max(0, col - k)
      max_row = min(row + k, rows - 1)
      max_col = min(col + k, cols - 1)

      # check left-top bound
      if(min_row > 0 and min_col > 0):
        result[row][col] = dp[max_row][max_col] + dp[min_row - 1][min_col - 1] - dp[min_row - 1][max_col] - dp[max_row][min_col - 1]
      # check left bound
      elif(min_row > 0):
        result[row][col] = dp[max_row][max_col] - dp[min_row - 1][max_col]
      # check top bound
      elif(min_col > 0):
        result[row][col] = dp[max_row][max_col] - dp[max_row][min_col - 1]
      else:
        result[row][col] = dp[max_row][max_col]

  return result


print(matrix_block_sum([
  [1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1],
], 1))
