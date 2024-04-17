def t_test(array_1, array_2):
  mean_1 = mean(array_1)
  mean_2 = mean(array_2)
  std_dev_1 = std_dev(array_1)
  std_dev_2 = std_dev(array_2)
  std_err = math.sqrt(((std_dev_1 ** 2) / len(array_1)) + ((std_dev_2 ** 2) / len(array_2)))

  return abs(mean_1 - mean_2) / std_err


sample_1 = [30, 45, 41, 38, 34, 36, 31, 30, 49, 50, 51, 46, 41, 37, 36, 34, 33, 49, 32, 46, 41, 44, 38, 50, 37, 39, 40, 46, 42]
sample_2 = [46, 49, 52, 55, 56, 40, 47, 51, 58, 46, 46, 56, 53, 57, 44, 42, 40, 58, 54, 53, 51, 57, 56, 44, 42, 49, 50, 55, 43]

print(t_test(sample_1, sample_2))
