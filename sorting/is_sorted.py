def is_sorted(array):
  for i in range(0, len(array) - 1, 1):
    if (array[i] > array[i + 1]):
      return False
  return True


print(is_sorted([0, 5, 7, 3, 1, 4, 8, 2, 9, 6]))
print(is_sorted([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
