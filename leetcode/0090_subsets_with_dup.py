# 90. Subsets II
# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

from typing import List
from collections import Counter

def subsetsWithDup(nums: List[int]) -> List[List[int]]:
  counter = Counter(nums)
  
  ret = [[]]
  
  for n, count in counter.items():
    tmp = []
    for i in range(count):
      tmp += [r + [n]*(i+1) for r in ret]
      
    ret += tmp
    
  return ret
    
  
  
nums=[1,2,2]

print(subsetsWithDup(nums))