# https://leetcode.com/problems/flipping-an-image/

# image must be square
# 1. reverse each row
# 2. invert each row

def flip_and_invert(image):
  size = len(image) # matrix size n*n
  mid = size // 2 # middle row index

  for row in range(0, size, 1):
    left = 0
    right = size - 1

    # inplace swap and flip bit
    while(left < right):
      temp = image[row][left]
      image[row][left] = image[row][right] # swap
      image[row][left] = (image[row][left] + 1) % 2 # flip

      image[row][right] = temp # swap
      image[row][right] = (image[row][right] + 1) % 2 # flip

      left += 1
      right -= 1

    # handle if row len is odd
    if(size % 2 != 0):
      image[row][mid] = (image[row][mid] + 1) % 2

  return image


print(flip_and_invert([[1,1,0],[1,0,1],[0,0,0]]))
