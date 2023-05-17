def one_dim_to_two_dim_array(original: list[int], rows: int, cols: int) -> list[list[int]]:
  if(rows * cols != len(original)):
    return []

  result = [[None] * cols for i in range(rows)]

  for i in range(0, rows * cols, 1):
    row = i // cols
    col = i % cols

    result[row][col] = original[i]

  return result


print(one_dim_to_two_dim_array(original = [1,2,3,4], rows = 2, cols = 2))
