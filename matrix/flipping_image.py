def flip_and_invert(image):
  n = len(image) # matrix size n*n
  m = n // 2 # middle row index

  for r in range(0, n, 1):
    i = 0
    j = n - 1

    # inplace swap and flip bit
    while(i < j):
      temp = image[r][i]
      image[r][i] = image[r][j]
      image[r][i] = (image[r][i] + 1) % 2

      image[r][j] = temp
      image[r][j] = (image[r][j] + 1) % 2

      i += 1
      j -= 1

    # handle if row len is odd
    if(n % 2 != 0):
      image[r][m] = (image[r][m] + 1) % 2

  return image


print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
