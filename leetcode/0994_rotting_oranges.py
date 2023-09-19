# 994. Rotting Oranges

# In a given grid, each cell can have one of three values:

# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

# Solution:
# BFS level by level from all rotten nodes 
# Return Max depth if no fresh orange exists

grid = [[2,1,1],[1,1,0],[0,1,1]]
# grid = [[1,2]]
# grid = [[1],[2]]

def orangesRotting(grid):
  nr, nc = len(grid), len(grid[0])

  def findAll(s):
    return [(i,j) for i in range(nr) for j in range(nc) if grid[i][j] == s]

  def neighbors(c, s):
    cx,cy = c
    n = [(cx+1,cy),(cx-1,cy),(cx,cy-1),(cx,cy+1)]
    return [(x,y) for (x,y) in n 
            if 0 <= x < nr and 0 <= y < nc and
            grid[x][y] == s]

  q = []
  q.extend(findAll(2))

  time = 0
  while q:
    adj = []
    while q: 
      for (x,y) in neighbors(q.pop(), 1): 
        grid[x][y] = 2
        adj.append((x,y))
    q.extend(adj)
    if q: time += 1

  return -1 if any(1 in row for row in grid) else time


print(orangesRotting(grid))
