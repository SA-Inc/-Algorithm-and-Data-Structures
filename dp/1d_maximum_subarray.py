def kadane(array):
  n = len(array)
  current_sum = 0
  max_sum = -999999

  # on each step get current and max sum from 0 to i
  # reset current sum if negative
  for i in range(0, n, 1):
    current_sum += array[i]
    max_sum = max(max_sum, current_sum)
    if(current_sum < 0):
      current_sum = 0

  return max_sum


a = [-1, 2, -2, 5, 7, -3, 1]

print(kadane(a))
