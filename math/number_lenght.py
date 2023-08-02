import math

def len_of_num(num: int):
  return math.ceil(math.log(num + 1) / math.log(10))


def num_to_digit_array(num):
  n = len_of_num(num)
  arr = [0] * n
  i = n - 1

  while(num != 0):
    arr[i] = num % 10
    num = num // 10
    i -= 1

  return arr


def digit_array_to_num(digits):
  n = len(digits)
  num = 0
  mul = 1

  for i in range(n - 1, -1, -1):
    num += (mul * digits[i])
    mul *= 10

  return num


print(len_of_num(184329))

a = num_to_digit_array(184329)

print(a)
print(digit_array_to_num(a))
