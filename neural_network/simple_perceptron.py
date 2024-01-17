import numpy as np

x = [0.4, 0.5, 0.4]
w = [0.4, 0.3, 0.6]
threshold = 0.5


def activation(weighted_sum):
  if(weighted_sum > threshold):
    return 1
  else:
    return 0


def perceptron(input_data, weights):
  weighted_sum = 0

  # np.dot alternative for this 1d array loop
  for x, w in zip(input_data, weights):
    weighted_sum += x * w

  # weighted_sum = np.dot(input_data, weights)
  # print(weighted_sum)

  return activation(weighted_sum)


output_data = perceptron(x, w)

print(output_data)
