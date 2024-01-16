import numpy as np


def activation(x):
  return 0 if x < 0.5 else 1


def perceptron(input_data):
  # weights of each neuron on the same layer
  hidden_1_1 = [0.3, 0.3, 0]
  hidden_1_2 = [0.4, -0.5, 1]

  # 2x3
  weights_1 = [hidden_1_1, hidden_1_2]
  # 1x2
  weights_2 = [-1, 1]

  # dot product weights and inputs
  # s = w * i
  # np.dot() function
  weights_sum = []
  for i in range(0, len(weights_1), 1):
    weights_layer_sum = 0
    for d in range(0, len(input_data), 1):
      weights_layer_sum += weights_1[i][d] * input_data[d]
    weights_sum.append(weights_layer_sum)

  # apply activation function for each weight sum
  out_hidden = []
  for i in range(0, len(weights_sum), 1):
    out_hidden.append(activation(weights_sum[i]))

  # dot product weights and output hidden
  weights_sum = 0
  for i in range(0, len(weights_2), 1):
    weights_sum += weights_2[i] * out_hidden[i]

  output_data = activation(weights_sum)
  return output_data


  # # numpy alternative
  # input_data = np.array(input_data)
  # sum_hidden = np.dot(weights_1, input_data)
  # out_hidden = np.array([activation(x) for x in sum_hidden])
  # sum_end = np.dot(weights_2, out_hidden)
  # output_data = activation(sum_end)
  # print(output_data)


have_house = 1
have_money = 0
have_phone = 1

input_data = [have_house, have_money, have_phone]

output_data = perceptron(input_data)

if(output_data == 1):
  print('ok')
else:
  print('no')
