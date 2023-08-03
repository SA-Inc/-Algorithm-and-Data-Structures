a = 5
b = 6

def is_set_bit(number, index):
  return (number & (1 << index)) != 0

def set_bit(number, index):
  return (number | (1 << index))

def reset_bit(number, index):
  return (number & ~(1 << index))

def inverse_bit(number, index):
  return (number ^ (1 << index))


print('a & b: {}'.format(a & b))
print('a | b: {}'.format(a | b))
print('a ^ b: {}'.format(a ^ b))


print(is_set_bit(6, 1))
print(set_bit(6, 3))
print(inverse_bit(6, 2))
print(reset_bit(6, 1))
