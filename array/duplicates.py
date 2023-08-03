# primitive version
def array_duplicates(array):
  result = set()
  for i in range(0, len(array), 1):
    for j in range(i + 1, len(array)):
      if(array[i] == array[j]):
        result.add(array[j])
  return list(result)


print(array_duplicates([1, 2, 3, 4, 2, 1, 5, 6, 1]))
