def longest_common_subsequence(str_1, str_2):
  rows = len(str_1)
  cols = len(str_2)

  # 1 - dp table
  dp = [[0] * (cols + 1) for _ in range((rows + 1))]
  path = [[None] * (cols + 1) for _ in range((rows + 1))]
  # 2 - base
  # dp[0][0] = 0

  # 4 - loop order
  for row in range(1, rows + 1, 1):
    for col in range(1, cols + 1, 1):
      # 3 - states formula
      if(str_1[row - 1] == str_2[col - 1]):
        dp[row][col] = 1 + dp[row - 1][col - 1]
        path[row][col] = (row - 1, col - 1, str_1[row - 1])
      else:
        # dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

        if(dp[row - 1][col] > dp[row][col - 1]):
          dp[row][col] = dp[row - 1][col]
          path[row][col] = (row - 1, col, '')
        else:
          dp[row][col] = dp[row][col - 1]
          path[row][col] = (row, col - 1, '')

  # compose result string from end
  result_string = ''
  # tuple with coord and char
  current = path[row][col]
  while(current is not None):
    result_string += current[2]
    current = path[current[0]][current[1]]

  # 5 - result
  return (dp[rows][cols], result_string[::-1])


s1 = 'AGGTAB'
s2 = 'GXTXAYB'

res = longest_common_subsequence(s1, s2)

print(res)
