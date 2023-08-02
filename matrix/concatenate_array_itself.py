def concatenate_array_itself(nums: list[int]) -> list[int]:
  ans = [None] * (2 * len(nums))

  for i in range(0, len(nums), 1):
    ans[i] = nums[i]
    ans[len(nums) + i] = nums[i]

  return ans


print(getConcatenation([1, 2, 3, 4, 5]))
