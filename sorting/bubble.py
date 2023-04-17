# compare two adjacent elements and swap if need
# on each iteration starts from 0 index

def bubble_sort(array):
  for outer in range(0, len(array) - 1, 1):
    for inner in range(0, len(array) - outer - 1, 1):
      if(array[inner] > array[inner + 1]):
        temp = array[inner]
        array[inner] = array[inner + 1]
        array[inner + 1] = temp

l  = [0, 5, 7, 3, 1, 4, 8, 2, 9, 6]

bubble_sort(l)
