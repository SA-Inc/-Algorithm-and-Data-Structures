def heapify(array, n, i):
  done = False

  while(done != True):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if(left < n and array[i] < array[left]):
      largest = left
    else:
      largest = i

    if(right < n and array[largest] < array[right]):
      largest = right

    if(largest != i):
      tmp = array[i]
      array[i] = array[largest]
      array[largest] = tmp
      i = largest
    else:
      done = True

def heap_sort_iterative(array):
  n = len(array)

  # build max heap
  for i in range(n // 2, -1, -1):
    heapify(array, n, i)

  # sort
  for i in range(n - 1, 0, -1):
    tmp = array[i]
    array[i] = array[0]
    array[0] = tmp
    heapify(array, i, 0)


c = [4, 1, 7, 2, 5, 9, 0, 8, 3, 6]
heap_sort_iterative(c)
print(c)
