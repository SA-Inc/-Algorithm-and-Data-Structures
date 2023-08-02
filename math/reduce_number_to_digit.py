def reduce_number_to_digit(num: int) -> int:
  digit_sum = 0

  while num > 0:
    digit_sum += num % 10
    num = num // 10

    if num == 0 and digit_sum > 9:
      num = digit_sum
      digit_sum = 0

  return digit_sum


print(reduce_number_to_digit(189))
