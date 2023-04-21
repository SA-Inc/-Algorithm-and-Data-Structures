def merge(nums1, len1, nums2, len2):
  while(len1 > 0 and len2 > 0):
    if(nums1[len1 - 1] > nums2[len2 - 1]):
      nums1[len1 + len2 - 1] = nums1[len1 - 1]
      len1 -= 1
    else:
      nums1[len1 + len2 - 1] = nums2[len2 - 1]
      len2 -= 1

  if(len2 > 0):
    nums1[:len2] = nums2[:len2]


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
len1 = 3
len2 = 3

res = merge(nums1, len1, nums2, len2)

print(nums1)
