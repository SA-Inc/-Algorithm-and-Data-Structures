# how many distinct ways can you climb to the top
def climb_stairs(n: int) -> int:
  # states
  dp = [None] * (n + 1)

  # base
  dp[0] = 1
  dp[1] = 1

  # move
  for i in range(2, n + 1, 1):
    # formula
    dp[i] = dp[i - 1] + dp[i - 2]

  # result
  return dp[n]


print(climb_stairs(5))
