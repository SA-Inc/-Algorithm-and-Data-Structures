def reverse(arr, left, right):
  while(left < right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    left += 1
    right -= 1
  return arr


# right rotate
def rotate(nums, step) -> None:
  n = len(nums)

  # prevent out of range (when step > n)
  step = step % n

  # 1. - reverse all array
  # 2. - reverse from array left side
  # 3. - reverse from array right side
  nums = reverse(nums, 0, n - 1)
  nums = reverse(nums, 0, step - 1)
  nums = reverse(nums, step, n - 1)

  return nums


a = [1, 2, 3, 4, 5, 6, 7]
k = 3

rotate(a, k)

print(a)
