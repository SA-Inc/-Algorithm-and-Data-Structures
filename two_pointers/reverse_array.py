def reverse(array):
  left = 0
  right = len(array) - 1

  # reverse in place by swaping
  while(left < right):
    temp = array[left]
    array[left] = array[right]
    array[right] = temp

    left += 1
    right -= 1

  return array


a = [1, 2, 3, 4, 5, 6]

reverse(a)

print(a)
