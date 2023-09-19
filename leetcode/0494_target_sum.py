# 494. Target Sum

# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

# Find out how many ways to assign symbols to make sum of integers equal to target S.

# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# There are 5 ways to assign symbols to make the sum of nums be target 3.
# N

def findTargetSumWays(nums, S):
  tot = sum(nums)
  if S > tot: return 0
  d = [0] * tot + [1] # tot is the max we can get, and there's one way to get it
  sums=set([tot]) # TODO, make this a dictionary? really a counter
  for a in reversed(nums):
    for k in sorted(sums):
      if k-2*a >= S:
        sums.add(k-2*a)
        d[k-2*a] += d[k]
  return d[S]

nums = [1, 1, 1, 1, 1]
S=3
print(findTargetSumWays(nums,S))
