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


def two_dim_to_one_dim_array(matrix):
  rows = len(matrix)
  cols = len(matrix[0])
  array = [0 for i in range(rows * cols)]

  for i in range(0, rows * cols, 1):
    row = i // cols
    col = i % cols
    array[i] = matrix[row][col]

  return array


print(two_dim_to_one_dim_array([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0, 0, 0]
]))
