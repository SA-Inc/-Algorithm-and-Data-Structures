data = [
  [50, 59, 3],
  [60, 69, 5],
  [70, 79, 9],
  [80, 89, 12],
  [90, 100, 8]
]

total_freq = 0
freq_middle_prod = 0

middle_array = []

for i in range(0, len(data), 1):
  lower = data[i][0]
  upper = data[i][1]
  freq = data[i][2]
  middle = (lower + upper) / 2
  middle_array.append(middle)

  total_freq += freq
  freq_middle_prod += middle * freq

mean = freq_middle_prod / total_freq

total_freq_dev = 0

for i in range(0, len(middle_array), 1):
  freq_dev = data[i][2] * ((middle_array[i] - mean) ** 2)
  total_freq_dev += freq_dev

std_dev = math.sqrt(total_freq_dev / (total_freq - 1))

print(std_dev)
