def change(money, amount):
  n = len(money)

  if(amount <= 0 and n <= 0):
    return 0

  lookup_table = [[None] * n for i in range(amount + 1)]

  for i in range(0, n, 1):
    lookup_table[0][i] = 1

  for i in range(1, amount + 1, 1):
    for j in range(0, n, 1):
      x = lookup_table[i - money[j]][j] if (i - money[j] >= 0) else 0
      y = lookup_table[i][j - 1] if (j >= 1) else 0

      lookup_table[i][j] = x + y

  print(lookup_table)

  return lookup_table[amount][n - 1]


m = [1, 5, 10, 20, 50]
a = 100

print(change(m, a))
