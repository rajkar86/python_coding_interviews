# Permutations

import collections

def permutation(nums):
  if not nums: return [[]]
  return [[n] + d 
          for i,n in enumerate(nums)
          for d in permutation(nums[:i]+nums[(i+1):])]
  
def permutationDup(nums):
  def helper(counter):
    if not counter: return [[]]
    res = []
    for n in counter:
      curr = counter.copy() # Shallow copy is okay here
      curr[n] -= 1
      if not curr[n]: del curr[n]
      res += [[n] + p for p in helper(curr)]
    return res
  return helper(collections.Counter(nums))


# permute is list all permutations
def permute(nums):
  
  ret = []
  used = set()
  
  def helper(res):
    
    if len(res) == len(nums): ret.append(res)
    
    for n in nums:
      if n in used: continue
      used.add(n)
      helper(res + [n])   
      used.remove(n)
      
  helper([])
  return ret


def permuteDup(nums):
  ret = []
  rem = collections.Counter(nums) 
  
  def helper(res):
    
    if len(res) == len(nums): ret.append(res)
    
    for n in rem: # loop over unique elements
      if not rem[n]: continue # Important check, the key will still exist when it's zero
      rem[n] -= 1
      helper(res + [n])   
      rem[n] += 1

  helper([])
  return ret



nums = [1,1,2] 
print(permutation(list(set(nums))))
print(permutationDup(nums))
