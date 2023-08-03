def stack_sort(stack):
  tmp_stack = []

  while(len(stack) != 0):
    pop_elem = stack.pop()

    while(len(tmp_stack) != 0 and pop_elem < tmp_stack[-1]):
      stack.append(tmp_stack.pop())
    tmp_stack.append(pop_elem)
  while(len(tmp_stack) != 0):
    stack.append(tmp_stack.pop())

  return stack


a = [1, 4, 7, 9, 2, 5, 7, 6]

print(stack_sort(a))
