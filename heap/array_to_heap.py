def heapify(array, n, i):
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
    heapify(array, n, largest)


def array_to_max_heap(array):
  n = len(array)
  start_index = n // 2 - 1
  for i in range(start_index, -1, -1):
    heapify(array, n, i)

max_heap = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(max_heap)
array_to_max_heap(max_heap)
print(max_heap)
