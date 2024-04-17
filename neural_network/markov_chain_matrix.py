import random

n = 12

states_name = ['I', 'have', 'big', 'car']
states_index = [0, 1, 2, 3]
# chain start node
states_probability = [0.5, 0.5, 0, 0]

transition_matrix = [
  [0.3, 0.2, 0, 0.5],
  [0.1, 0.4, 0, 0.5],
  [0.8, 0, 0.2, 0],
  [0.4, 0.05, 0.5, 0.05]
]

# get start node
current_state_index = random.choices(population = states_index, weights = states_probability)[0]

statistics = {}

for i in range(0, n, 1):
  print(states_name[current_state_index])

  # save to statistics
  if(states_name[current_state_index] in statistics):
    statistics[states_name[current_state_index]] += 1
  else:
    statistics[states_name[current_state_index]] = 1

  # get random row - next node index
  next_state_index = random.choices(population = states_index, weights = transition_matrix[current_state_index])[0]

  current_state_index = next_state_index


print('------------')
for k, v in statistics.items():
  print(k, v, v * 100 / n, '%')
