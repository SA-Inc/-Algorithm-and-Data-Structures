def exponential_search(array, search):
  n = len(array)

  if(n == 0):
    return -1

  search_range = 1

  # like jump search, but step increases rapidly
  while(search_range < n and array[search_range] < search):
    search_range *= 2

  # perform binary search
  left_index = search_range // 2
  right_index = min(search_range, n - 1)

  while(left_index <= right_index):
    middle_index = (left_index + right_index) // 2

    if(array[middle_index] == search):
      return middle_index
    elif(array[middle_index] < search): # change left bound
      left_index = middle_index + 1
    elif(array[middle_index] > search): # change right bound
      right_index = middle_index - 1

  return -1


a  = [0, 5, 7, 3, 1, 4, 8, 2, 9, 6]

a.sort()

print(exponential_search(a, 67))
