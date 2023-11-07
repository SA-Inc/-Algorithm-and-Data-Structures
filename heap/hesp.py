# restore heap invariant, base on i node (a[i] looks like root)
# if a[i] more than his children, nothing to do, sub-tree already heap
# else swap a[i] with largest child, and perform heapify for this child
def heapify(array, n, i):
  largest = i
  left = 2 * i + 1
  right = 2 * i + 2

  # decide which child larger
  if(left < n and array[largest] < array[left]):
    largest = left

  if(right < n and array[largest] < array[right]):
    largest = right

  # swap child with sub-root
  if(largest != i):
    tmp = array[i]
    array[i] = array[largest]
    array[largest] = tmp
    heapify(array, n, largest)


# if call heapify from last element to first, array turn in to heap
# heapify do nothing if i > n // 2 - 1 (no children, therefore no need call function)
# all elements (sub tree) more than i index after call heapify will be heap
def build(array):
  n = len(array)
  start_index = n // 2 - 1
  for i in range(start_index, -1, -1):
    heapify(array, n, i)


# swap root with last element and exclude it from heap (len - 1)
# call heapify for remain elements
def heap_sort(array):
  build(array)
  for i in range(len(array) - 1, 0, -1):
    tmp = array[i]
    array[i] = array[0]
    array[0] = tmp
    heapify(array, i, 0)


# like build heap
def insert(array, value):
  n = len(array)
  if(n == 0):
    array.append(value)
  else:
    array.append(value);
    start_index = n // 2 - 1
    for i in range(start_index, -1, -1):
      heapify(array, n, i)


def delete(array, value):
  n = len(array)
  i = 0
  for i in range(0, n, 1):
    if(value == array[i]):
      break

  tmp = array[i]
  array[i] = array[n - 1]
  array[n - 1] = tmp

  array.remove(value)

  start_index = n // 2 - 1
  for i in range(start_index, -1, -1):
    heapify(array, n, i)



a = [1, 2, 3, 4, 5]

build(a)

insert(a, 6)
insert(a, 7)
insert(a, 8)
insert(a, 9)

delete(a, 2)
delete(a, 5)

print(a)

# heap_sort(a)

# print(a)
