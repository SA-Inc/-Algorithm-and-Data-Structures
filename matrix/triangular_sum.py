# reduce array to single value as triangle
# if sum value >= 10 omit tens
# [1, 2, 3, 4, 5]
# [3, 5, 7, 9]
# [8, 2, 6]
# [0, 8]
# [8]


def triangular_sum(nums: list[int]) -> int:
  n = len(nums)

  for s in range(n, 0, -1):
    for i in range(0, s - 1, 1):
      nums[i] = (nums[i] + nums[i + 1]) % 10

  return nums[0]


print(triangular_sum([1, 2, 3, 4, 5]))
