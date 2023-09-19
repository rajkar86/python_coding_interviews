# 75. Sort Colors
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note: You are not suppose to use the library's sort function for this problem.


  
from typing import List

def sortColors(nums: List[int]) -> None:

  def countingSort(nums):
    lo, hi = min(nums), max(nums)
    count = [0] * (hi - lo + 1)

    for n in nums:
      count[n-lo] += 1

    for i in range(1,len(count)):
      count[i] += count[i-1]

    out = [0] * len(nums)
    for n in reversed(nums): # reversed only important for stable sort when you extend to radix
      out[count[n-lo]-1] = n
      count[n-lo] -= 1

    return out

  nums[:]=countingSort(nums)
  
nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)