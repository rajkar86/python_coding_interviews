# 327. Count of Range Sum

# Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
# Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

# Note:
# A naive algorithm of O(n2) is trivial. You MUST do better than that.

# Example:

# Input: nums = [-2,5,-1], lower = -2, upper = 2,
# Output: 3 
# Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.

      
nums = [-2,5,-1] 
low = -2
up = 2

import itertools

def countRangeSum(nums, low, up):
  def mergeSort(a): 
    count = 0
    if len(a) > 1:
      mid = len(a) // 2
      L, R = a[:mid], a[mid:]
      count = mergeSort(L) + mergeSort(R)

      ## Special code 'Divide and conquer' start
      i,j = 0,0
      for l in L:
        while i < len(R) and R[i] < (l + low): i += 1
        while j < len(R) and R[j] <= (l + up): j += 1
        count += j - i
      ## Special code end

      for i in reversed(range(len(a))):
        if L and R:
          t = L if L[-1] > R[-1] else R
        else:
          t = L if L else R
        a[i] = t.pop()

    return count

  return(mergeSort([0] + list(itertools.accumulate(nums))))

print(countRangeSum(nums, low, up))


# TODO need to understand better
# TODO BIT / Segment tree solution