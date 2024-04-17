def median(array):
  n = len(array)
  if(n % 2 == 0):
    return (array[(n // 2)] + array[(n // 2 - 1)]) // 2
  else:
    return array[n // 2]


def q1_q2_q3(array):
  array.sort()
  middle = len(array) // 2
  q1 = median(a[:middle])
  q2 = median(a)
  q3 = median(a[middle:])
  iqr = q3 - q1
  return (q1, q2, q3, iqr)


def is_outlier(quartile, num):
  lower = quartile[0] - 1.5 * quartile[3]
  upper = quartile[2] + 1.5 * quartile[3]
  if(num < lower or num > upper):
    return True
  else:
    return False


a = [7, 11, 14, 5, 8, 27, 16, 10, 13, 17, 16]
# a = [16, 18, 28, 13, 50, 31, 25, 22, 18, 23, 29, 38]

q = q1_q2_q3(a)

print(q)
print(is_outlier(q, max(a)))
print(is_outlier(q, min(a)))
