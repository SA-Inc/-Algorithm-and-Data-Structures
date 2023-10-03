import random

a = ['a', 'b', 'c', 'd', 'e', 'f']
n = len(a)

for i in range(n - 1, 0, -1):
  r = random.randint(0, i + 1)

  t = a[i]
  a[i] = a[r]
  a[r] = t


print(a)
