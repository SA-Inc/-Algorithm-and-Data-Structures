# looks like comb
# 1. check if not sorted in two inner loops, perform swap
# 2. check flag, if not sorted repeat inner loops

def even_odd_sort(array):
  is_sorted = False

  while(is_sorted == False):
    is_sorted = True

    # compare 0, 2, 4, ... indexes - even
    for i in range(0, len(array) - 1, 2):
      if(array[i] > array[i + 1]):
        temp = array[i]
        array[i] = array[i + 1]
        array[i + 1] = temp
        is_sorted = False

    # compare 1, 3, 5, ... indexes - odd
    for i in range(1, len(array) - 2, 2):
      if(array[i] > array[i + 1]):
        temp = array[i]
        array[i] = array[i + 1]
        array[i + 1] = temp
        is_sorted = False


# on each iteration compare even elements and odd elements
# if visualise it is look like brick wall

def even_odd_sort(array):
  for outer in range(0, len(array), 1):
    # if even return 1, if odd return 0
    inner = 1 if(outer % 2 == 0) else 0
    for inner in range(inner, len(array) - 1, 2):
      if(array[inner] > array[inner + 1]):
        temp = array[inner]
        array[inner] = array[inner + 1]
        array[inner + 1] = temp


l  = [0, 5, 7, 3, 1, 4, 8, 2, 9, 6]

even_odd_sort(l)

print(l)
