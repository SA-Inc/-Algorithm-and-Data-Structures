def monotonic_inc_stack(arr):
  n = len(arr)

  stack = []

  for i in range(0, n, 1):
    while(len(stack) > 0 and stack[len(stack) - 1] >= arr[i]):
      stack.pop()
    stack.append(arr[i])

  return stack


def monotonic_dec_stack(arr):
  n = len(arr)

  stack = []

  for i in range(0, n, 1):
    while(len(stack) > 0 and stack[len(stack) - 1] <= arr[i]):
      stack.pop()
    stack.append(arr[i])

  return stack



a1 = [2, 3, 7, 11, 5, 17, 19]
r1 = monotonic_inc_stack(a1)
print(r1)

a2 = [2, 3, 7, 11, 5, 17, 19]
r2 = monotonic_dec_stack(a2)
print(r2)
