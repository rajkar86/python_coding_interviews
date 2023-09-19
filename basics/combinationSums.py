from typing import List

# Combinations

from typing import List
import collections

# duplicates, no reuse
def combinationSumDFS(nums, target): 
  nums.sort() # To help with dup check later
  N, res = len(nums), []
  def helper(lo, t, path):
    if t == 0: res.append(path) 
    if t < 0: return
    for i in range(lo, N):
      if i > lo and nums[i] == nums[i-1]: # For dup; NOTE nums[lo] can be num[lo-1]
        continue 
      helper(i+1, t-nums[i], path + [nums[i]])
      
  helper(0, target, [])
  return res      

# no duplicates, no reuse
# If there are duplicates, 
# we don't want to get results that treat the same number as different
# target 4 can be [1*,3], [1+,3], if we have {1*,1+,3}
def combinationSum(nums, target): 
  dic = collections.defaultdict(lambda: [])
  dic[0] =[[]] 
  for n in nums: 
    for i in reversed(range(n,target+1)): # remove reversed if infinite reuse
      if i-n in dic:
        dic[i] += [[n] + d for d in dic[i-n]] 

  return dic[target] if target in dic else []


## DFS might be better in this case
def combinationSumDup(nums, target):
  counter = collections.Counter(nums) # diff
  dic = collections.defaultdict(lambda: [])
  dic[0] =[[]] 
  for key, count in counter.items():
    new = collections.defaultdict(lambda: []) # temp  
    for times in range(1,count+1):            # while looping over times
      n = key * times  
      curr = [key] * times
      for i in reversed(range(n,target+1)):
        if i-n in dic:
          new[i] += [curr + d for d in dic[i-n]]
    for k in set(dic) | set(new): dic[k] += new[k]

  return dic[target] if target in dic else []


def permutationSum(nums, target):  # with infinite reuse!
  res = [1]
  for i in range(1,target+1): 
    res.append(sum(res[i - n] for n in nums if i >= n))
  return res[-1]


## TODO permutationSum without reuse -- backtracking, anything better possible??



nums = [1,3,2,1] 
target = 4

print(combinationSumDFS(list(set(nums)), target))
print(combinationSumDFS(nums, target))
print(combinationSum(set(nums), target))
print(combinationSumDup(nums, target))

print(permutationSum(set(nums), target))
