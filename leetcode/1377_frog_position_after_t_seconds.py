# 1377. Frog Position After T Seconds

# Given an undirected tree consisting of n vertices numbered from 1 to n. A frog starts jumping from the vertex 1. In one second, the frog jumps from its current vertex to another unvisited vertex if they are directly connected. The frog can not jump back to a visited vertex. In case the frog can jump to several vertices it jumps randomly to one of them with the same probability, otherwise, when the frog can not jump to any unvisited vertex it jumps forever on the same vertex. 

# The edges of the undirected tree are given in the array edges, where edges[i] = [fromi, toi] means that exists an edge connecting directly the vertices fromi and toi.

# Return the probability that after t seconds the frog is on the vertex target. 

n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
t = 2
target = 4

def frogPosition(n, edges, t, target):
  g = [set() for _ in range(n)]
  for e in edges:
    g[e[0]-1].add(e[1]-1)
    g[e[1]-1].add(e[0]-1)

  prob = [1] + [0] * (n-1) 
  visited = set([0])

  for _ in range(t):
    prob_new = [0] * n
    for i, p in enumerate(prob):
      if p > 0:
        nbs = g[i] - visited
        visited.update(nbs)
        deg = len(nbs)
        if deg > 0:
          for nb in nbs: prob_new[nb] += prob[i]/deg 
        else:
          prob_new[i] += prob[i]
    prob = prob_new

  return prob[target-1]

print (frogPosition(n, edges, t, target))
        
    
  
