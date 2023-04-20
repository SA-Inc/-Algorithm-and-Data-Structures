def interval_intersection(first_list, second_list):
  # input: list[list[int]], list[list[int]]
  # output: list[list[int]]

  result = []

  first_pointer = 0
  second_pointer = 0

  # loop until both array lenght
  while(first_pointer < len(first_list) and second_pointer < len(second_list)):
    # check if intervals ends or begins not at each other
    # if second ends before first starts
    if(second_list[second_pointer][1] < first_list[first_pointer][0]):
      second_pointer += 1
    # if first ends before second starts
    elif(first_list[first_pointer][1] < second_list[second_pointer][0]):
      first_pointer += 1
    # if both interval have intersection
    else:
      # interval start - max from begins, end - min from ends
      result.append([
        max(first_list[first_pointer][0], second_list[second_pointer][0]),
        min(first_list[first_pointer][1], second_list[second_pointer][1])
      ])

      # inc pointer that ends first
      if(first_list[first_pointer][1] < second_list[second_pointer][1]):
        first_pointer += 1
      else:
        second_pointer += 1

  return result


first_list = [[0,2],[5,10],[13,23],[24,25]]
second_list = [[1,5],[8,12],[15,24],[25,26]]

res = interval_intersection(first_list, second_list)

print(res)
