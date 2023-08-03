def truth_table(n):
  table = []
  for i in range(0, 2 ** n, 1):
    line = tuple((i // 2 ** j % 2 for j in range(n - 1, -1, -1)))
    table.append(line)
  return table


t = truth_table(3)

print(t)
