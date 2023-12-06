def dutch_flag(array):
  n = len(array)
  left = 0
  mid = 0
  right = n - 1

  # ranges
  # from 0 to left - 0
  # from left to mid - 1
  # from mid to right - 0, 1 or 2
  # from right to n - 2

  # mid - current element
  # from most left to most right bound
  while(mid <= right):
    # move 0 to left and inc left and mid
    if(array[mid] == 0):
      tmp = array[mid]
      array[mid] = array[left]
      array[left] = tmp
      left += 1
      mid += 1
    # 1 stay at middle of flag, inc mid
    elif(array[mid] == 1):
      mid += 1
    # move 2 to right and dec right
    elif(array[mid] == 2):
      tmp = array[mid]
      array[mid] = array[right]
      array[right] = tmp
      right -= 1

  return array



# a = [1, 1, 0, 2, 0, 2, 1, 2, 0, 1, 2, 2]
a = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
# a = [0, 1, 2, 0, 1, 2]

print(dutch_flag(a))
