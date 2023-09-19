# Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

def singleNumber(nums: list) -> int:
  r = [~0, 0, 0] # r[i] counts of bits that have appeared i times (-1 or ~0 is all ones in binary)
  for n in nums:
      r = [(r[i-1 % 3] & n) | (r[i] & ~n) for i in range(len(r))]
  print(r)
  return r[1]

a = [2,2,3,2,3,3,4]
#a = [0,1,0,1,0,1,99]
print(singleNumber(a))
