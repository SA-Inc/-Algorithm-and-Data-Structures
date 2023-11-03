def print_circular_array(array, start_index, n):
  array_len = len(array)
  for i in range(start_index, n + start_index, 1):
    print(array[(i % array_len)])


a = [1, 2, 3, 4, 5]

print_circular_array(a, 3, 10)
