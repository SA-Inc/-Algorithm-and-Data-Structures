def sort_table_by_col(score: list[list[int]], col: int) -> list[list[int]]:
  rows = len(score)

  # insertion sort
  for row in range(1, rows, 1):
    key_row = score[row]

    new_row = row - 1

    while(new_row >= 0 and score[new_row][col] < key_row[col]):
      score[new_row + 1] = score[new_row]
      new_row -= 1

    score[new_row + 1] = key_row

  return score


print(sort_table_by_col(score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], col = 2))
