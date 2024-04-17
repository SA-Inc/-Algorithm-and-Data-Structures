import math

def percentile(array, n):
  array.sort()
  k = (len(array) - 1) * n
  f = math.floor(k)
  c = math.ceil(k)
  if(f == c):
    return array[int(k)]
  d0 = array[int(f)] * (c - k)
  d1 = array[int(c)] * (k - f)
  return d0 + d1


a = [42, 54, 65, 47, 59, 40, 53]
print(percentile(a, 0.50))
