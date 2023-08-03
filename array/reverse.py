def array_reverse_stack(array):
  stack = []
  result = []
  for i in range(0, len(array), 1):
    stack.append(array[i])
  for i in range(0, len(stack), 1):
    result.append(stack.pop())
  return result


def array_reverse_end(array):
  result = []
  for i in range(len(array) - 1, -1, -1):
    result.append(array[i])
  return result


def array_reverse_swap(array):
  left_index = 0
  right_index = len(array) - 1
  while (left_index < right_index):
    temp = array[left_index]
    array[left_index] = array[right_index]
    array[right_index] = temp

    left_index += 1
    right_index -= 1
  return array


a = [1, 2, 3, 4, 5, 6]

print(array_reverse_stack(a))
print(array_reverse_end(a))
print(array_reverse_swap(a))
