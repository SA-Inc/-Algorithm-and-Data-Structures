# https://leetcode.com/problems/special-positions-in-a-binary-matrix/

def num_special(mat: list[list[int]]) -> int:
  def is_special(cell_row, cell_col, rows, cols):
    # check row
    for col in range(0, cols, 1):
      if(cell_col != col and mat[cell_row][col] == 1):
        return False

    # check col
    for row in range(0, rows, 1):
      if(cell_row != row and mat[row][cell_col] == 1):
        return False

    return True


  rows = len(mat)
  cols = len(mat[0])
  special_nums = 0

  for row in range(0, rows, 1):
    for col in range(0, cols, 1):
      if(mat[row][col] == 1):
        if(is_special(row, col, rows, cols) == True):
          special_nums += 1

  return special_nums


print(num_special(mat = [[1,0,0],[0,0,1],[1,0,0]]))
