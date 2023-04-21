# loop 2d array as 1d array
m = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0, 0, 0]
]

rows = len(m)
cols = len(m[0])

for i in range(0, rows * cols, 1):
  row = i // cols
  col = i % cols

  print(m[row][col])
