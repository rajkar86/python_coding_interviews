# Prefix sum in a changing array
class BinaryIndexedTree(object):
  def __init__(self, nums):
    self.nums = nums
    self.sums = [0] * (len(nums) + 1)
    
  def add(self, i, addVal): 
    self.nums[i] += addVal
    i += 1 # sums is 1-indexed
    while i < len(self.sums):
      self.sums[i] += addVal
      i += i & -i

  def set(self, i, val):
    self.add(i, val - self.nums[i])
  
  def sum(self, i):  ## From id 0 to i in nums, 1 to i+1 in sums
    i += 1 # sums is 1-indexed
    r = 0
    while i > 0:
      r += self.sums[i]
      i -= i & -i ### Least significant bit
    return r

