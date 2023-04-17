# we "know" the position and "do not know" value
# because search value

def selection_sort(array):
  for i in range(0, len(array), 1):
    # find min value on right side and store index
    min_index = i
    for j in range(i, len(array), 1):
      if(array[j] < array[min_index]):
        min_index = j

    # place min index value at left side position
    temp = array[i]
    array[i] = array[min_index]
    array[min_index] = temp


l  = [0, 5, 7, 3, 1, 4, 8, 2, 9, 6]

selection_sort(l)

print(l)
