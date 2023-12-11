# find pivot point
# split array into two left and right sub arrays
# perform binary search

def binary_search_rotated(array, num):
  n = len(array)
  left = 0
  right = len(array) - 1

  # pivot - previous element grater
  # if rotation in left side - left element grater that middle
  # else - left side sorted and middle grater that right
  while(left < right):
    middle = (left + right) // 2
    if(array[middle] > array[right]):
      left = middle + 1
    else:
      right = middle

  pivot = left
  left = 0
  right = len(array) - 1

  # choose left or right sub array
  if(array[pivot] <= num and num <= array[right]):
    left = pivot
  else:
    right = pivot


  while(left <= right):
    middle = (left + right) // 2

    # found
    if(array[middle] == num):
      return middle

    if(array[middle] < num):
      left = middle + 1
    else:
      right = middle - 1

  return -1
