#174. Dungeon Game

# The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

# The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

# Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

# In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

import itertools

def calculateMinimumHP(dungeon):
  m, n = len(dungeon), len(dungeon[0])
  for i,j in itertools.product(reversed(range(m)), reversed(range(n))):
    prev = min(dungeon[i+1][j] if i<m-1 else float('inf'), 
               dungeon[i][j+1] if j<n-1 else float('inf'))
    if i==m-1 and j == n-1: prev = 1
    dungeon[i][j] = max(prev - dungeon[i][j],1)
  return dungeon[0][0]

dungeon=[[-2,-3,3],[-5,-10,1],[10,30,-5]]
print(calculateMinimumHP(dungeon))
