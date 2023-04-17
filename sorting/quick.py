# lomuto partition

def partition(array, left, right):
  # most right index
  pivot_index = right
  # index for result pivot (border btw two subsets)
  store_index = left

  # move bigger elements to right (smaller stay on left)
  # move result pivot index to left
  for i in range(left, right, 1):
    if(array[i] <= array[pivot_index]):
      temp = array[i]
      array[i] = array[store_index]
      array[store_index] = temp
      store_index += 1

  temp = array[pivot_index]
  array[pivot_index] = array[store_index]
  array[store_index] = temp

  return store_index


# divide array into two subarrays by pivot index
# smaller elements should be on left side to pivot
# bigger elements should be on right side to pivot
# repeat for left and right subarrays
def quick_sort(array, left, right):
  if(left < right):
    pivot_index = partition(array, left, right)
    quick_sort(array, left, pivot_index - 1)
    quick_sort(array, pivot_index + 1, right)


l  = [0, 5, 7, 3, 1, 4, 8, 2, 9, 6]

quick_sort(l, 0, len(l) - 1)

print(l)
