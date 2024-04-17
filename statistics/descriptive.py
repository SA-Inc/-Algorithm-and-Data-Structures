import math


def mode(array):
  d = {}
  for i in range(0, len(array), 1):
    if(array[i] in d):
      d[array[i]] += 1
    else:
      d[array[i]] = 1

  return dict(sorted(d.items(), key = lambda x:x[1], reverse = True))


def mean(array):
  return sum(array) / len(array)


def median(array):
  mid = len(array) // 2
  if(len(array) % 2 == 0):
    return sum(sorted(array)[mid - 1:mid + 1]) / 2
  else:
    return sorted(array)[mid]


def min_max_range(array):
  min_val = min(array)
  max_val = max(array)
  range_val = max_val - min_val
  return (min_val, max_val, range_val)


def variance(array):
  mean_val = mean(array)
  var = 0

  for i in range(0, len(array), 1):
    var += ((array[i] - mean_val) ** 2)

  return var / (len(array) - 1)


def std_dev(array):
  var = variance(array)
  return math.sqrt(var)


def cv(array):
  sd_val = std_dev(array)
  mean_val = mean(array)
  return sd_val / mean_val


a = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]
print(cv(a))
