# 278. First Bad Version
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer

def isBadVersion(version):
  return True

class Solution:
    def firstBadVersion(self, n):
      
      lo = 0
      hi = n
      while lo < hi:
        mid = (lo + hi)//2 
        if not isBadVersion(mid):
          lo = mid + 1
        else:
          hi = mid
        
      return lo


### STD: Binary search variant 

