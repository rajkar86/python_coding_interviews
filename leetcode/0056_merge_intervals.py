# 56. Merge Intervals

# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

intervals=[[1,3], [2,6],[8,10],[15,18]]

def merge(intervals):
  intervals = sorted(intervals, key = lambda x: x[0])
  
  ret = [intervals[0]]
  
  for i in range(1, len(intervals)):
    curr = intervals[i]
    if ret[-1][1] >= curr[0]:
      ret[-1][1] = max(curr[1], ret[-1][1]) # handles 2 cases: overlapping as well as contained in interval
    else:
      ret.append(curr)
    
  return (ret)


def merge_in_place(intervals):
  intervals = sorted(intervals, key = lambda x: x[0])

  p = 0

  for i in range(1, len(intervals)):
    curr = intervals[i]
    ret = intervals[p]
    if ret[1] >= curr[0]:
      ret[1] = max(curr[1], ret[1])
    else:
      p += 1
      intervals[p] = intervals[i] ## Be careful when you write

  return (intervals[:(p+1)])

  
  
  
print(merge(intervals))