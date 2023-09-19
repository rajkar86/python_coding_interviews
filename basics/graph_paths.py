import collections, heapq
from math import inf

def graph_from_edges_w(edges, undirected = False):
  graph = collections.defaultdict(list)
  for u, v, w in edges:
    graph[u].append((v, w))
    if undirected: 
      graph[v].append((u, w))
  return graph

def djikstra(edges, source, undirected = False):
  graph = graph_from_edges_w(edges, undirected)

  pq = [(0,source)]
  dist = {source:0}
  seen = set() # also need this; because a node can be added multiple times

  while pq:
    dcurr, node = heapq.heappop(pq)
    
    if node in seen: continue
    seen.add(node)

    for nb, w in graph[node]:
      dcalc = dcurr + w
      if dist.get(nb, inf) > dcalc: 
        dist[nb] = dcalc
        heapq.heappush(pq, (dcalc, nb))
    
  return dist

def bellman_ford(n, edges, source, undirected = False): 
  dist = {source:0} 
  
  for _ in range(n-1): 
    for (u,v,w) in edges:  
      if u in dist:
        dist[v] = min(dist.get(v,inf), dist[u] + w)
      if undirected and v in dist: 
        dist[u] = min(dist.get(u,inf), dist[v] + w)
  
  return dist
