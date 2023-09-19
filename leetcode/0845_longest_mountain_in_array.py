# 845. Longest Mountain in Array

# Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

# B.length >= 3
# There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
# (Note that B could be any subarray of A, including the entire array A.)

# Given an array A of integers, return the length of the longest mountain. 

# Return 0 if there is no mountain.

# Example 1:

# Input: [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
# Example 2:

# Input: [2,2,2]
# Output: 0

def longestMountain(A: List[int]) -> int:    
  n = len(A)
  if n < 3: return 0

  def find_inc(it):
    ret = [0]
    prev = next(it)
    for curr in it:
      ret.append(ret[-1] + 1 if prev < curr else 0)
      prev = curr
    return ret # TODO use yield

  up_from_left = find_inc(iter(A))
  up_from_right = find_inc(reversed(A))

  ret = 0
  for l,r in zip(iter(up_from_left), reversed(up_from_right)):
    if l and r: ret = max(ret, l + r + 1)

  return ret