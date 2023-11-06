def max_heapify(array, n, i):
  largest = i
  left = 2 * i + 1
  right = 2 * i + 2

  if(left < n and array[largest] < array[left]):
    largest = left

  if(right < n and array[largest] < array[right]):
    largest = right

  if(largest != i):
    tmp = array[i]
    array[i] = array[largest]
    array[largest] = tmp
    max_heapify(array, n, largest)


def min_heapify(array, n, i):
  smallest = i
  left = 2 * i + 1
  right = 2 * i + 2

  if(left < n and array[smallest] > array[left]):
    smallest = left

  if(right < n and array[smallest] > array[right]):
    smallest = right

  if(smallest != i):
    tmp = array[i]
    array[i] = array[smallest]
    array[smallest] = tmp
    min_heapify(array, n, smallest)


def build_max_heap(array):
  n = len(array)
  start_index = n // 2 - 1
  for i in range(start_index, -1, -1):
    max_heapify(array, n, i)


def build_min_heap(array):
  n = len(array)
  start_index = n // 2 - 1
  for i in range(start_index, -1, -1):
    min_heapify(array, n, i)


a = [3,9,2,1,4,5]
build_max_heap(a)
print(a)


a = [3,9,2,1,4,5]
build_min_heap(a)
print(a)
