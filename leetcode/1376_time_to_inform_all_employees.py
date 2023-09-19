# 1376. Time Needed to Inform All Employees

# A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company has is the one with headID.

# Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also it's guaranteed that the subordination relationships have a tree structure.

# The head of the company wants to inform all the employees of the company of an urgent piece of news. He will inform his direct subordinates and they will inform their subordinates and so on until all employees know about the urgent news.

# The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e After informTime[i] minutes, all his direct subordinates can start spreading the news).

# Return the number of minutes needed to inform all the employees about the urgent news.

n = 15
headID = 0
manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]

# n = 6 
# headID = 2 
# manager = [2,2,-1,2,2,2]
# informTime = [0,0,1,0,0,0]


def numOfMinutes(n, headID, manager, informTime):

  subs = [[]] * n

  for e, m in enumerate(manager):
    if m >= 0:
      subs[m] = subs[m] + [e]
  max_time = 0

  def helper(m, t):
    nonlocal max_time    # nonlocal if it's primitive
    sub = subs[m]
    if len(sub) == 0:
      max_time = max(max_time, t)

    t += informTime[m] 
    for e in sub:
      helper(e, t)

  helper(headID, 0)
  return max_time


print(numOfMinutes(n, headID, manager, informTime))
