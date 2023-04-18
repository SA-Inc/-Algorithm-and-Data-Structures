def linear_search(array, search):
  for i in range(0, len(array), 1):
    if (array[i] == search):
      return i
  return -1


a  = [0, 5, 7, 3, 1, 4, 8, 2, 9, 6]

print(linear_search(a, 3))
