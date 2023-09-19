# 207. Course Schedule

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?


from collections import deque

numCourses = 2
prerequisites = [[1,0]]

def canFinish(numCourses, prerequisites):
  n = numCourses
  g =[[] for _ in range(n)]
  indeg = [0] * n
  res = []

  for e in prerequisites:
    indeg[e[0]] += 1
    g[e[1]].append(e[0]) 


  q = deque(filter(lambda v: indeg[v] == 0 , range(n)))
        
  while q:
    node = q.pop()
    res.append(node)
    for n in g[node]:
      indeg[n] -= 1
      if indeg[n] == 0: q.append(n)

  return len(res) == numCourses

print(canFinish(numCourses, prerequisites))
