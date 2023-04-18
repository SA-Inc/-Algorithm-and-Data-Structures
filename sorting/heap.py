def heapify(array, n, i):
  root = i
  left = 2 * i + 1
  right = 2 * i + 2

  if(left < n and array[left] > array[root]):
    root = left

  if(right < n and array[root] < array[right]):
    root = right

  if(root != i):
    tmp = array[i]
    array[i] = array[root]
    array[root] = tmp
    heapify(array, n, root)


def heap_sort(array):
  # make heap from array
  for i in range(len(array) // 2 - 1, -1, -1):
    heapify(array, len(array), i)

  for i in range(len(array) - 1, -1, -1):
    # pop elements. move current root to end
    tmp = array[i]
    array[i] = array[0]
    array[0] = tmp
    heapify(array, i, 0)


l  = [0, 5, 7, 3, 1, 4, 8, 2, 9, 6]

heap_sort(l)

print(l)
