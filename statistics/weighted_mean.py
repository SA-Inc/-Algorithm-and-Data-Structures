a = [16, 20, 12, 16, 16, 10, 16, 20, 24, 20]

w = {}

# calc freq
for i in range(0, len(a), 1):
  if(a[i] in w):
    w[a[i]] += 1
  else:
    w[a[i]] = 1

w_sum = 0

# weighted product sum
for key, value in w.items():
  w_sum += key * value

# mean
print(w_sum / len(a))
