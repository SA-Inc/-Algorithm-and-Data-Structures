def sliding_window_max_sum(arr, k):
  n = len(arr)

  if(n < k):
    return 0

  window_total = 0

  for i in range(0, k, 1):
    window_total += arr[i]

  max_total = window_total

  for i in range(k, n, 1):
    window_total += arr[i] - arr[i - k]
    max_total = max(max_total, window_total)

  return max_total


print(sliding_window_sum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))
print(sliding_window_sum([100, 200, 300, 400], 2))
print(sliding_window_sum([2, 3], 3))
