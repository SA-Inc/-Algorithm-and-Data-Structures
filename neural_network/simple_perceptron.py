weights = [0.2, -0.1]
bias = -0.29
learning_rate = 0.01


def learn(input_data, label):
  for i in range(0, len(input_data), 1):
    # print(input_data[i], label[i])

    # w * i
    input_weights_sum = 0
    for w in range(0, len(weights), 1):
      input_weights_sum += input_data[i][w] * weights[w]

    input_weights_sum += bias
    predict = 1 if input_weights_sum > 0 else 0
    error = label[i] - predict

    # print(input_weights_sum, predict, error)

    for w in range(0, len(weights), 1):
      weights[w] += learning_rate * error * input_data[i][w]


learn_input_data = [
  [1, 1],
  [2, 2],
  [4, 4],
  [5, 5]
]

learn_output_data = [0, 0, 1, 1]

predict_input_data = [5, 4]


learn(learn_input_data, learn_output_data)
print(weights)
