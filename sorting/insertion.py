# we "know" the value and "do not know" position
# because search insertion position

def insertions_sort(array):
  for i in range(1, len(array), 1):
    # take value on right side
    value = array[i]
    j = i
    # search insertion position on left side
    while(j > 0 and array[j - 1] > value):
      array[j] = array[j - 1]
      j -= 1

    array[j] = value


l  = [0, 5, 7, 3, 1, 4, 8, 2, 9, 6]

insertions_sort(l)

print(l)
