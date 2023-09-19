# We are given an array A of positive integers, and two positive integers L and R (L <= R).

# Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least L and at most R.

# Example :
# Input: 
# A = [2, 1, 4, 3]
# L = 2
# R = 3
# Output: 3
# Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
    

    
def numSubarrayBoundedMax(a, l, r):
  
  def countWithMaxBelow(m):
    count=0
    curr=0
    for i in a:
      if i<=m:
        curr += 1
        count += curr
      else:
        curr=0
    return (count)
      
  return (countWithMaxBelow(r) - countWithMaxBelow(l-1))
  
ans = numSubarrayBoundedMax([2, 1, 4, 3], 2, 3)
print (ans)
