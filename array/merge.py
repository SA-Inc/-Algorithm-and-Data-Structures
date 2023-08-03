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
