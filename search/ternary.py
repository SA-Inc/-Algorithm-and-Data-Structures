def ternary_search(array, search):
  left_index = 0
  right_index = len(array) - 1

  while(left_index <= right_index):
    left_middle_index = left_index + (right_index - left_index) // 3
    right_middle_index = right_index - (right_index - left_index) // 3

    if(search == array[left_middle_index]):
      return left_middle_index
    if(search == array[right_middle_index]):
      return right_middle_index

    if(array[right_middle_index] < search):
      left_index = left_middle_index + 1
    elif(array[left_middle_index] > search):
      right_index = right_middle_index - 1
    else:
      left_index = left_middle_index + 1
      right_index = right_middle_index - 1

  return -1


a  = [0, 5, 7, 3, 1, 4, 8, 2, 9, 6]

a.sort()

print(ternary_search(a, 3))
