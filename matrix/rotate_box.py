def rotate_box(box: list[list[str]]) -> list[list[str]]:
  # rotate by 90 clockwise
  rows = len(box)
  cols = len(box[0])

  # rotated box
  rotated = [['.'] * rows for _ in range(cols)]

  # empty = .
  # wall = *
  # stone = #

  # two pointers method
  # move by orginal box rows
  for row in range(0, rows, 1):
    right = cols - 1
    for left in range(cols - 1, -1, -1):
      # check left and right side if possible move stone
      if(box[row][left] != '.'):
        if(box[row][left] == '*'):
          right = left
        # pass to rotated box
        rotated[right][rows - row - 1] = box[row][left]
        right -= 1

  return rotated


print(rotate_box(box = [
  ["#",".","*","."],
  ["#","#","*","."]
]))
