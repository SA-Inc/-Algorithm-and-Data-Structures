import math

def array_min(array):
  min_value = math.inf
  for i in range(0, len(array), 1):
    if (array[i] < min_value):
      min_value = array[i]
  return min_value

def array_max(array):
  max_value = -math.inf
  for i in range(0, len(array), 1):
    if (array[i] > max_value):
      max_value = array[i]
  return max_value

def array_min_index(array):
  min_value = math.inf
  min_value_index = None
  for i in range(0, len(array), 1):
    if (array[i] < min_value):
      min_value = array[i]
      min_value_index = i
  return (min_value_index, min_value)

def array_max_index(array):
  max_value = -math.inf
  max_value_index = None
  for i in range(0, len(array), 1):
    if (array[i] > max_value):
      max_value = array[i]
      max_value_index = i
  return (max_value_index, max_value)


a = [1, 2, 3, 4, 2, 1, 5, 6, 1]

print(array_min(a))
print(array_min_index(a))
print(array_max(a))
print(array_max_index(a))
