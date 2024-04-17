def stem_leaf(array):
  array.sort()
  n = len(array)
  d = {}

  for i in range(0, n, 1):
    stem = array[i] // 10
    leaf = array[i] % 10

    if(stem in d):
      d[stem].append(leaf)
    else:
      d[stem] = []
      d[stem].append(leaf)

  return d


d = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 ]
print(stem_leaf(d))
