def merge(array, left, mid, right):
  left_size = mid - left + 1
  right_size = right - mid

  left_array = [None] * left_size
  right_array = [None] * right_size

  for i in range(0, left_size, 1):
    left_array[i] = array[left + i]
  for i in range(0, right_size, 1):
    right_array[i] = array[mid + 1 + i]

  i = 0
  j = 0
  k = left

  while(i < left_size and j < right_size):
    if(left_array[i] < right_array[j]):
      array[k] = left_array[i]
      i += 1
    else:
      array[k] = right_array[j]
      j += 1
    k += 1

  while(i < left_size):
    array[k] = left_array[i]
    i += 1
    k += 1

  while(j < right_size):
    array[k] = right_array[j]
    j += 1
    k += 1


def merge_sort(array, left, right):
  if(left < right):
    mid = (left + right) // 2
    merge_sort(array, left, mid)
    merge_sort(array, mid + 1, right)
    merge(array, left, mid, right)


l  = [0, 5, 7, 3, 1, 4, 8, 2, 9, 6]

merge_sort(l, 0, len(l) - 1)

print(l)
