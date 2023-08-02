# sum of max deleted value per row
def delete_greatest_value(grid: list[list[int]]) -> int:
  rows = len(grid)
  cols = len(grid[0])

  total_sum = 0

  while(cols != 0):
    max_row = 0

    for i in range(0, rows, 1):
      # find max value
      max_row_value = max(grid[i])
      max_row_index = grid[i].index(max_row_value)

      # mark col as deleted
      grid[i][max_row_index] = 0

      max_row = max(max_row, max_row_value)

    total_sum += max_row

    cols -= 1

    print(grid)

  return total_sum


grid = [
  [1,2,4],
  [3,3,1]
]

print(delete_greatest_value(grid))
