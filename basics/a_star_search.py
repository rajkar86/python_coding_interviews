# A star search with a consistent heuristic
# consistent - h(n) <= cost(n,nb) + h(nb) for all neighbors nb of node n
# Just admissible - never overestimates

from collections import defaultdict
from heapq import heappush, heappop
import math

def a_star(
  start, #node
  goal, #fn, node -> bool
  heuristic, #fn, node -> int (consistent heuristic)
  neighbors, #fn, node -> generator
  edgeCost, #fn, node, node -> int
):
  
  q = []
  heappush(q, (0,start))
  
  closed = set() # NOT seen list
  
  dist = defaultdict(lambda: math.inf) # curr best, g(x)
  dist[start] = 0
  
  parent = {}
  def get_path(n):
    if n==start: return [n]
    return get_path(parent[n]) + [n]

  while q:
    _, n = heappop(q)
    d = dist[n]
    
    if n in closed: continue 
    closed.add(n) # Don't add to closed below, like for seen list
    
    if goal(n): 
      return d, get_path(n)
    
    for nb in neighbors(n):
      dcalc = edgeCost(n, nb) + d
      if dcalc < dist[nb]: 
        # Won't happen for visited nodes if heuristic is consistent
        # If heuristic is only admissible, also remove from closed set here  
        parent[nb] = n
        dist[nb] = dcalc
        f = dcalc + heuristic(nb)
        heappush(q, (f, nb))
        # Actually need to re-prioritize okay 

  return None, None


# Compare Djikstra

def djikstra(graph, source, undirected = False):

  pq = [(0,source)]
  dist = {source:0}
  seen = set() # also need this; because a node can be added multiple times

  while pq:
    dcurr, node = heappop(pq)
    
    if node in seen: continue
    seen.add(node)

    for nb, w in graph[node]:
      dcalc = dcurr + w
      if dist.get(nb, math.inf) > dcalc: 
        dist[nb] = dcalc
        heappush(pq, (dcalc, nb))
    
  return dist