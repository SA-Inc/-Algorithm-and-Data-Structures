def binary_search(array, search):
  left_index = 0
  right_index = len(array) - 1

  while(left_index <= right_index):
    middle_index = (left_index + right_index) // 2

    if (array[middle_index] == search):
      return middle_index

    # change left bound
    elif (array[middle_index] < search):
      left_index = middle_index + 1

    # change right bound
    elif (array[middle_index] > search):
      right_index = middle_index - 1

  return -1


a  = [0, 5, 7, 3, 1, 4, 8, 2, 9, 6]

a.sort()

print(binary_search(a, 3))
