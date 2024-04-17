def frequency(array):
  # value, count, frequency
  array.sort()
  n = len(array)
  d = {}
  total = 0

  for i in range(0, n, 1):
    if(array[i] in d):
      d[array[i]][0] += 1
      total += 1
    else:
      d[array[i]] = [0, 0]
      d[array[i]][0] = 1
      total += 1

  for key, val in d.items():
    val[1] = val[0] / total

  return d


a = [2, 3, 5, 3, 6, 8, 7, 8, 3, 3, 5, 3, 7, 3, 8, 5, 2, 7, 8, 3]
print(freq(a))
