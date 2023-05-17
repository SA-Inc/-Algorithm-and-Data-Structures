# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

def number_of_beams(bank: list[str]) -> int:
  # each device send and receive lines
  devices = [None] * len(bank)
  beams = 0

  # count laser devices on each line
  for i in range(0, len(bank), 1):
    devices[i] = bank[i].count('1')

  # if next line has 0 devices, move prev line device on this line
  # else multiply sender and receiver lines
  for i in range(0, len(devices) - 1, 1):
    # print(devices, i)
    if(devices[i + 1] == 0):
      devices[i + 1] = devices[i]
    else:
      beams += devices[i] * devices[i + 1]

  return beams


print(ones_minus_zeros(grid = [[0,1,1],[1,0,1],[0,0,1]]))
