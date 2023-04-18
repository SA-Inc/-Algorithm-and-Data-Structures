def interpolation_search(array, search):
  left_index = 0
  right_index = len(array) - 1

  while((left_index <= right_index) and (array[left_index] < search) and (search < array[right_index])):
    # zero division protection
    if(array[left_index] == array[right_index]):
      break

    a = right_index - left_index # y1 - y0
    b = array[right_index] - array[left_index] # x1 - x0
    c = search - array[left_index] # x - x0
    d = left_index # y0
    # middle index = y

    # y = y0 + (x - x0) * ((y1 - y0) / (x1 - x0))

    middle_index = d + (c * (a // b))

    if(array[middle_index] == search):
      return middle_index
    elif(array[middle_index] < search): # change left bound
      left_index = middle_index + 1
    elif(array[middle_index] > search): # change right bound
      right_index = middle_index - 1

  if(array[left_index] == search):
    return left_index
  if(array[right_index] == search):
    return right_index

  return -1


a  = [0, 5, 7, 3, 1, 4, 8, 2, 9, 6]

a.sort()

print(interpolation_search(a, 5))
