# array must be sorted

def two_sum(nums, target):
  left = 0
  right = len(nums) - 1

  while(left < right):
    if (nums[left] + nums[right] == target):
      return [left, right]
    if (nums[left] + nums[right] < target):
      left += 1
    else:
      right -= 1

  return [-1, -1]


res = two_sum(nums = [2,7,11,15], target = 13)

print(res)
