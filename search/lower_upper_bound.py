def lower_bound_linear(array, value):
  for i in range(0, len(array), 1):
    if(array[i] >= value):
      return i
  return -1


def lower_bound_binary(array, value):
  lower = 0
  upper = len(array) - 1
  result = -1

  while(lower <= upper):
    middle = (lower + upper) // 2

    # check smaller element, can be result
    # check left side
    if(array[middle] >= value):
      upper = middle - 1
      result = middle
    # check right side
    else:
      lower = middle + 1

  return result


def upper_bound_linear(array, value):
  for i in range(0, len(array), 1):
    if(array[i] > value):
      return i
  return len(array)


def upper_bound_binary(array, value):
  lower = 0
  upper = len(array) - 1
  result = len(array)

  while(lower <= upper):
    middle = (lower + upper) // 2

    # check smaller element, can be result
    # check left side
    if(array[middle] > value):
      upper = middle - 1
      result = middle
    # check right side
    else:
      lower = middle + 1

  return result

a = [0, 1, 1, 2, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 9, 9, 9, 9]

# print(lower_bound_linear(a, 2))
# print(lower_bound_linear(a, 10))

# print(lower_bound_binary(a, 2))
# print(lower_bound_binary(a, 9))
# print(lower_bound_binary(a, 9))

print(upper_bound_linear(a, 9))

print(upper_bound_binary(a, 2))
