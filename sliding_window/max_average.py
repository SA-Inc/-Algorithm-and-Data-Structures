def find_max_average(nums, k):
  window_sum = 0

  # calc window
  for i in range(0, k, 1):
    window_sum += nums[i]

  result = window_sum

  # move window
  for i in range(k, len(nums), 1):
    window_sum += nums[i] - nums[i - k]
    result = max(window_sum, result)

  return result / k

a = [1,2,3,2,5,6]

res = find_max_average(a, 2)

print(res)
