def max_water_area(height):
  left = 0
  right = len(height) - 1
  max_area = 0

  if(len(height) <= 2):
    return min(height)

  while(left < right):
    if(height[left] < height[right]):
      box_width = right - left
      area = box_width * height[left]
      max_area = max(max_area, area)
      left += 1
    else:
      box_width = right - left
      area = box_width * height[right]
      max_area = max(max_area, area)
      right -= 1

  return max_area


height = [1,8,6,2,5,4,8,3,7]

res = max_water_area(height)

print(res)
