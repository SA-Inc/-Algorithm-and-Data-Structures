#  O(n2)
def array_pairs_sum_unoptimized(array, pair_sum):
  n = len(array)
  pairs = []
  for i in range(0, n, 1):
    for j in range(0, n, 1):
      if ((array[i] + array[j]) == pair_sum):
        pairs.append((array[i], array[j]))
  return pairs


# O(n.log(n))
def array_pairs_sum_sort(array, pair_sum):
  array.sort()

  pairs = []
  n = len(array)
  low = 0
  high = n - 1

  while (low < high):
    if (array[low] + array[high] == pair_sum):
      pairs.append((array[low], array[high]))
    if (array[low] + array[high] < pair_sum):
      low += 1
    else:
      high -= 1

  return pairs


a = [1, 2, 4, 6, 3, 7, 8]

print(array_pairs_sum_unoptimized(a, 10))
print(array_pairs_sum_sort(a, 10))
