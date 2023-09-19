# 959. Regions Cut By Slashes


# In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.

# (Note that backslash characters are escaped, so a \ is represented as "\\".)

# Return the number of regions.

grid =[
  " /",
  "/ "
]


from collections import defaultdict

def regionsBySlashes(grid):
  N = len(grid)
  V = 4*N*N
  g = defaultdict(set)
    
  def nbs(c, i, j, k):
    idx = 4*(i*N + j) + k
    def add(x):
      g[idx].add(x)
      g[x].add(idx)      
    if k == 0 and c != "\\": add(idx+1)
    if k == 0 and c != "/" : add(idx+3)
    if k == 1 and c != "/" : add(idx+1)
    if k == 2 and c != "\\": add(idx+1)
    if k == 2 and i is not (N-1): add(idx + 4*N -2)
    if k == 3 and j is not (N-1): add(idx + 2)
      
  for i, row in enumerate(grid):
    for j, c in enumerate(row):
      for k in range(4):
        nbs(c, i, j, k)
  
  seen = [0] * V
  def dfs(x):
    seen[x] = 1
    for n in g[x]:
      if not seen[n]: dfs(n)
    return 1
  
  return sum(dfs(v) for v in range(V) if not seen[v])

print(regionsBySlashes(grid))
    
    
    
  
  
