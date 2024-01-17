import numpy as np


def activation(x):
  return 0 if x < 0.5 else 1


def perceptron(input_data):
  # weights of each neuron on the same layer
  hidden_1 = [0.3, 0.3, 0]
  hidden_2 = [0.4, -0.5, 1]

  # 2x3
  weights_1 = [hidden_1, hidden_2]
  # 1x2
  weights_2 = [-1, 1]

  input_data = np.array(input_data)
  weights_1_sum = np.dot(weights_1, input_data)
  hidden_layer_output = np.array([activation(x) for x in weights_1_sum])
  weights_2_sum = np.dot(weights_2, hidden_layer_output)
  output_data = activation(weights_2_sum)

  return output_data


have_house = 1
have_money = 0
have_phone = 1

input_data = [have_house, have_money, have_phone]

output_data = perceptron(input_data)

if(output_data == 1):
  print('ok')
else:
  print('no')
