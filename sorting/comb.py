# sort on distance, on each iteration reduce window
# when window = 1, make bubble sort

def comb_sort(array):
  factor = 1.247
  window = len(array) - 1

  while(window >= 1):
    i = 0
    while(i + window < len(array)):
      if(array[i] > array[i + window]):
        temp = array[i]
        array[i] = array[i + window]
        array[i + window] = temp
      i += 1
    window = int(window / factor)

  for outer in range(0, len(array) - 1, 1):
    for inner in range(0, len(array) - outer - 1, 1):
      if(array[inner] > array[inner + 1]):
        temp = array[inner]
        array[inner] = array[inner + 1]
        array[inner + 1] = temp


l  = [0, 5, 7, 3, 1, 4, 8, 2, 9, 6]

comb_sort(l)

print(l)
