# left pointer moves faster than right

def move_zeroes(nums):
  right = 0

  for left in range(0, len(nums), 1):
    # compare current (left) and previous (right)
    if(nums[left] != 0 and nums[right] == 0):
      temp = nums[left]
      nums[left] = nums[right]
      nums[right] = temp

    if(nums[right] != 0):
      right += 1

  return nums


a = [1, 0, 3, 4, 0, 6, 7]

move_zeroes(a)

print(a)
