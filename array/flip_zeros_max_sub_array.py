def flip_bits(array):
  n = len(array)
  ones = 0

  # turn 1 to -1, count ones, turn 0 to 1
  for i in range(0, n, 1):
    if(array[i] == 1):
      array[i] = -1
      ones += 1
    else:
      array[i] = 1

  # kandanes algorithm of max sub array sum
  current_sum = 0
  max_sum = 0

  left = 0
  right = 0
  s = 0

  for i in range(0, n, 1):
    current_sum += array[i]

    if(max_sum < current_sum):
      max_sum = current_sum
      left = s
      right = i

    # because temporary current sum can be 0
    if(current_sum <= 0):
      current_sum = 0
      s = i + 1

  print(array)
  return (left, right, ones + max_sum)

# a = [1, 1, 0, 0, 1, 1]
a = [0, 1, 0, 0, 0, 1]

print(flip_bits(a))
