# Subsets is really list all combinations

from collections import Counter

# Complexity is O(N*2^N) 2^N lists, times N elements (N/2)
def subsetsDp(nums):
  
  ret = [[]]
  
  for n in nums:
    ret += [r+[n] for r in ret]
  
  return (ret)
  
def subsetsWithDupDp(nums):
  
  counter = Counter(nums)
  ret = [[]] # Do not forget empty set
  
  for n, count in counter.items():
    tmp = []
    for i in range(count):
      tmp += [r + [n]*(i+1) for r in ret]
      
    ret += tmp
    
  return ret


def subsets_bitmask(nums):
  
  ret = []
  
  n = len(nums)
  
  for s in range(2**n): ## 2**n == 1 >> n
    l = []
    
    ## s in binary number will be of length n where i-th place is 1 if we have to include that nums[i] 
    mask = 1
    for i in range(n):
      if s & mask: l.append(nums[i])
      mask <<= 1
    ret.append(l)
  
  return (ret)


def subsetsDup(nums): 
  ret = []
  n = len(nums)
  nums.sort() ## Only for dup
  def helper(start, res):
    ret.append(res)
    for i in range(start,n):
      if i > start and nums[i] == nums[i-1]: continue # Only for dup
      helper(i+1, res + [nums[i]])          
    
  helper(0, [])
  return ret


nums = [1,1,2] 