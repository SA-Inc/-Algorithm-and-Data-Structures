def kadane(array):
  n = len(array)
  current_sum = 0
  max_sum = -999999

  # start, end subarray index
  left = 0
  right = 0
  # tmp offset for start index
  s = 0

  # on each step get current and max sum from 0 to i
  # reset current sum if negative
  for i in range(0, n, 1):
    current_sum += array[i]

    # move left and right
    if(max_sum < current_sum):
      max_sum = current_sum
      left = s
      right = i

    # move tmp offset to right
    if(current_sum < 0):
      current_sum = 0
      s = i + 1

  return (left, right, max_sum)


a = [-1, 2, -2, 5, 7, -3, 1]

print(kadane(a))
