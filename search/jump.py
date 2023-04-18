from math import sqrt

# main idea - skip subarrays to find range with out search number
# then use linear search
def jump_search(array, search):
  n = len(array)
  # iteration step
  jump_step = int(sqrt(n))
  # index of previous position
  previous_step = 0

  # iterate by big step and find range where element is
  while(array[min(jump_step, n) - 1] < search):
    previous_step = jump_step
    jump_step += int(sqrt(n))

    # out of bounds (end of array)
    if(previous_step >= n):
      return -1

  # linear search in founded range
  while(array[previous_step] < search):
    previous_step += 1

    # out of bounds (next block or end of array)
    if(previous_step == min(jump_step, n)):
      return -1

  if(array[previous_step] == search):
    return previous_step

  return -1


a  = [0, 5, 7, 3, 1, 4, 8, 2, 9, 6]

a.sort()

print(jump_search(a, 54))
