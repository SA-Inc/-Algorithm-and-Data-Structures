def array_count_elements(array):
  count = {}
  for i in range(0, len(array), 1):
    if ((array[i] in count) == False):
      count[array[i]] = 1
    else:
      count[array[i]] += 1
  return count


print(array_count_elements([1, 2, 3, 4, 2, 1, 5, 6, 1]))
