def prefix_sum(array):
  n = len(array)
  dp = [None] * n
  dp[0] = array[0]

  for i in range(1, n, 1):
    dp[i] = dp[i - 1] + array[i]

  return dp


def suffix_sum(array):
  n = len(array)
  dp = [None] * n
  dp[n - 1] = array[n - 1]

  for i in range(n - 2, -1, -1):
    dp[i] = dp[i + 1] + array[i]

  return dp


a = [1, 2, 3, 4, 5]

print(prefix_sum(a))
print(suffix_sum(a))
