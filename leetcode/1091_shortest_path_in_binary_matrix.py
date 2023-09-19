# 1091. Shortest Path in Binary Matrix

# In an N by N square grid, each cell is either empty (0) or blocked (1).

# A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

# Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
# C_1 is at location (0, 0) (ie. has value grid[0][0])
# C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
# If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
# Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

grid = [[0,0,0],[1,1,0],[1,1,0]]
# grid = [[0,1],[1,0]]

from collections import defaultdict
from itertools import product
from heapq import heappush, heappop

def shortestPathBinaryMatrix(grid):
  nr, nc = len(grid), len(grid[0])

  def neighbors(c):
    for dx,dy in product([-1,0,1],[1,0,-1]):
      x,y = c[0]+dx, c[1]+dy
      if (0 <= x < nr and 0 <= y < nc and 
      (x,y) != c and grid[x][y]==0):
        yield (x,y)
        
  def heuristic(c):
    return max(abs(nr-1-c[0]), abs(nc-1-c[1]))
    

  if not grid or not grid[0]: return -1
  if grid[0][0] == 1: return -1

  start = (0,0)
  
  q = []
  heappush(q, (0,start))
  
  closed = set() # NOT seen list
  
  dist = defaultdict(lambda: float('inf')) # curr best, g(x)
  dist[start] = 1

  while q: 
    p, n = heappop(q)
    d = dist[n]
    
    if n in closed: continue 
    closed.add(n) # Don't add to closed below, like for seen list
    
    if n == (nr-1,nc-1): 
      return d
    
    for nb in neighbors(n):
      new_dist = 1 + d
      if new_dist < dist[nb]: 
        # Won't happen for visited nodes if heuristic is consistent
        # If heuristic is only admissible, also remove from closed set here  
        dist[nb] = new_dist
        f = new_dist + heuristic(nb)
        heappush(q, (f, nb))
        # Actually need to re-prioritize okay 

  return -1

def shortestPathBinaryMatrixBFS(grid):
  nr, nc = len(grid), len(grid[0])

  def neighbors(c):
    cx,cy = c[0], c[1]
    n = [(cx+x,cy+y) for x,y in product([-1,0,1],[1,0,-1])]
    return [(x,y) for x,y in n 
            if 0 <= x < nr and 0 <= y < nc 
            and (x,y) != (cx,cy)
            and grid[x][y]==0]

  # print(neighbors((0,0)))
  
  if not grid or not grid[0]: return -1
  if grid[0][0] == 1: return -1
  
  q = [(0,0)]
  seen = set([(0,0)])
  dist = defaultdict(lambda: float('inf')) # curr best, g(x)
  dist[(0,0)] = 1

  for n in q:
    d = dist[n]
    if n == (nr-1,nc-1): return d
    for nb in neighbors(n):
      if nb not in seen:
        q.append(nb)
        seen.add(nb)
        dist[nb] = d + 1

  return -1
print(shortestPathBinaryMatrix(grid)) # A star
print(shortestPathBinaryMatrixBFS(grid))
