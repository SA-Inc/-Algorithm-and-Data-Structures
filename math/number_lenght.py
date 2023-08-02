import math

def len_of_num(num: int):
  return math.ceil(math.log(num + 1) / math.log(10))


print(len_of_num(184329))
