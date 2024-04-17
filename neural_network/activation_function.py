import numpy as np


def sigmoid(x):
  return 1 / (1 + np.exp(-x))


def binary_step(x):
  # return 0 if x.all() < 0 else 1
  return np.heaviside(x, 0)


def hyperbolic_tangent(x):
  return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))


def relu(x):
  return np.maximum(x, 0)


y = np.array([[0], [1], [1], [0]])

a = np.array([
  [1,2,3],
  [-1,-2,-3],
  [5,6,9],
  [7,4,5]
])

print(sigmoid(y))

print(binary_step(a))

print(hyperbolic_tangent(y))

print(relu(a))
