# both arrays must have equal length

def array_merge(array1, array2):
  array1_len = len(array1)
  array2_len = len(array2)
  result = [False for i in range(array1_len + array2_len)]

  i = 0
  j = 0
  k = 0

  while (i < array1_len):
    result[k] = a[i]
    i += 1
    k += 1

  while (j < array1_len):
    result[k] = b[j]
    j += 1
    k += 1

  return result


a = [1, 2, 3]
b = [4, 5, 6]

print(array_merge(a, b))



# merge different size arrays

def merge(num1, num2):
  arr3 = [None]*(len(num1)+len(num2))
  i, j, k = 0, 0, 0

  while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
      arr3[k] = arr1[i]
      k += 1
      i += 1
    else:
      arr3[k] = arr2[j]
      k += 1
      j += 1

  while i < len(num1):
    arr3[k] = arr1[i];
    k += 1
    i += 1

  while j < len(num2):
    arr3[k] = arr2[j];
    k += 1
    j += 1

  return arr3

arr1 = [1, 3]
arr2 = [2]
print(merge(arr1, arr2))

arr1 = [1, 3, 4, 5]
arr2 = [2, 4, 8]
print(merge(arr1, arr2))

arr1 = [5, 9]
arr2 = [4, 7, 8]
print(merge(arr1, arr2))
