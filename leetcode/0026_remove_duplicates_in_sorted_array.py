# 26. Remove Duplicates from Sorted Array
# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        for i in range(1, len(nums)):
          if nums[i] != nums[p]:
            p = p + 1
            nums[p] = nums[i]

        return p + 1