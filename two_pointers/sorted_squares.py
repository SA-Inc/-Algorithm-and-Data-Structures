# input arraty must be sorted

def sorted_squares(nums):
  result = [None] * len(nums)
  left = 0
  right = len(nums) - 1
  move = len(nums) - 1

  while(left <= right):
    if(abs(nums[left]) > abs(nums[right])):
      result[move] = nums[left] ** 2
      left += 1
    else:
      result[move] = nums[right] ** 2
      right -= 1

    move -= 1

  return result


a = [1, 2, 3, 4, 5, 6, 7]

res = sorted_squares(a)

print(res)
