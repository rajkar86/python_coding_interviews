# 805. Split Array With Same Average

# In a given integer array A, we must move every element of A to either list B or list C. (B and C initially start empty.)

# Return true if and only if after such a move, it is possible that the average value of B is equal to the average value of C, and B and C are both non-empty.

# Example :
# Input: 
# [1,2,3,4,5,6,7,8]
# Output: true
# Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average of 4.5.
# Note:

# The length of A will be in the range [1, 30].
# A[i] will be in the range of [0, 10000].

A = [1,2,3,4,5,6,7,8]
A = [5,3,11,19,2]
#A=[2,12,18,16,19,3]
#A = [3,1]


def splitArraySameAverage(A):

  N = len(A)
  S = sum(A)
  M = N//2 + 1 
  # The smaller partition is utmost M

  target = {} # smaller partition size -> required total for that size
  for i in range(1,M): 
    if (S * i) % N == 0:
      target[i] = (S*i)//N
      
  if len(target) == 0:
    return False
  

  ## mat i shows how many sums can be create with n numbers
  mat = [set() for i in range(M)]  
  mat[0].add(0)

  for i, num in enumerate(A):
    for k in reversed(range(1,min(i+2,M))):  # reversed is important
      mat[k].update([i + num for i in mat[k-1]])
      if k in target and target[k] in mat[k]:
        return True
  
  return False

def splitArraySameAverageBitset(A):

  N,S = len(A),sum(A)
  M = N//2 + 1

  target = {}
  for i in range(1,M): 
    if (S * i) % N == 0:
      target[i] = (1 << (S*i)//N)
      
  if len(target) == 0:
    return False
  
  v = [1] + [0] * (M-1)

  for i, num in enumerate(A):
    for k in reversed(range(1,min(i+1,M))):
      v[k] |= (v[k-1] << num)
      if (k in target) and (target[k] & v[k]):
        return True
        
  return False


print(splitArraySameAverage(A))
print(splitArraySameAverageBitset(A))
