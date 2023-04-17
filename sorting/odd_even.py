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
