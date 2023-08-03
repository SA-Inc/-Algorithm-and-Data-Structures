def array_right_rotate(array, times):
  for t in range(0, times, 1):
    last = array[len(array) - 1]
    for i in range(len(array) - 2, -1, -1):
      array[i + 1] = array[i]
    array[0] = last
  return array


def array_left_rotate(array, times):
  for t in range(0, times, 1):
    first = array[0]
    for i in range(0, len(array) - 1, 1):
      array[i] = array[i + 1]
    array[len(array) - 1] = first
  return array


a = [1, 2, 3, 4, 5, 6]

print(array_right_rotate(a, 2))
print(array_left_rotate(a, 1))
