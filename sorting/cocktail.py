# improved bubble
# looks like two-pointer technique

def cocktail_sort(array):
  left = 0
  right = len(array) - 1

  while(left <= right):
    # from end to start
    for i in range(right, left, -1):
      if(array[i - 1] > array[i]):
        temp = array[i]
        array[i] = array[i - 1]
        array[i - 1] = temp
    left += 1

    # from start to end
    for i in range(left, right, 1):
      if(array[i] > array[i + 1]):
        temp = array[i]
        array[i] = array[i + 1]
        array[i + 1] = temp
    right -= 1


l  = [0, 5, 7, 3, 1, 4, 8, 2, 9, 6]

cocktail_sort(l)

print(l)
