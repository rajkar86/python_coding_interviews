# 80. Remove Duplicates from Sorted Array II
# Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

from typing import List

def removeDuplicates(nums: List[int]) -> int:
  
  j = 0
  count = 0
  
  for i,n in enumerate(nums):
    if i==0 or nums[i] != nums[i-1]:
      count = 0
    count += 1
    
    if count > 2:
      continue
      
    nums[j] = n
    j+= 1
      
  del nums[j:]
  return j
  
  
nums = [1,1,1,2,2,3]
print(removeDuplicates(nums))
print(nums)

