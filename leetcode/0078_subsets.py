# 78. Subsets
# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.


from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
  
  ret = [[]]
  
  for n in nums:
    ret += [r+[n] for r in ret]
  
  return (ret)
  
### Complexity is O(N*2^N)

def subsets_bitmask(nums: List[int]) -> List[List[int]]:
  
  ret = []
  
  n = len(nums)
  
  for s in range(1 >> n): ## 2**n == 1 >> n
    l = []
    
    ## s in binary number will be of length n where i-th place is 1 if we have to include that nums[i] 
    mask = 1
    for i in range(n):
      if s & mask: l.append(nums[i])
      mask <<= 1
    ret.append(l)
  
  return (ret)
  
if __name__ =="__main__":
  import timeit
  a = timeit.timeit('subsets([1,2,3,4])', globals=globals(), number=100)
  b = timeit.timeit('subsets_bitmask([1,2,3,4])', globals=globals(), number=100)
  print(a,b)