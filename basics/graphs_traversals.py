# Graph tricks

from collections import deque, defaultdict, Counter
from typing import List, Set, Dict


def graph_from_edges(edges, undirected = False):
  adj = defaultdict(set) ## list if order of neighbors is important
  for x, y in edges:
    adj[x].add(y)
    if undirected: adj[y].add(x)
  return adj

adj = graph_from_edges([])

def get_nodes_in_graph(g):
  nodes = set(g.keys())
  for v in g.values(): nodes.update(v)
  return nodes ### Note that this won't include nodes with no edges (obviously)

#dfs 
#TODO in backtracking, often you set seen inside the edges loop and check if it's not seen at the beginning of the function 
#TODO have example in this format
seen = set()          
def dfs(x):
  seen.add(x)

  for y in adj[x]:
    if y not in seen:  ## NOTE - can’t do set difference 
      dfs(y)

# Also, it you care about all edges(e.g. cloning a tree, or all paths in a directed, acyclic graph) don't use global seen, mark visited and unmark after visiting neighbors
# seen is a mechanism to avoid visiting **nodes** twice

#bfs
seen = set()
def bfs(x):  
  seen.add(x)
  q = deque([x])

  while q:
    n = q.popleft() ## pop() would make it dfs
    nb = adj[n] - seen
    seen.update(nb) 
    q.extend(nb)  ## reversed(nb) if you want dfs-recursion order where nb is a list

#bfs using list
seen = set()
def bfsList(x):  
  q = [x]
  seen.add(q)

  for n in q: # Just iterate
    nb = adj[n] - seen
    seen.update(nb) 
    q.append(nb) # extend?

def topologicalSort(g, nodes):

  deg = defaultdict(int) # Better than Counter because of Counter's relation to zero
  for n in g:
    for nb in g[n]:
      deg[nb] += 1

  q = list(filter(lambda j: deg[j] == 0, nodes))

  for n in q:
    for nb in g[n]:
      deg[nb] -= 1
      if deg[nb] == 0: q.append(nb)

  return q

def findCyclesBFS(g: Dict[int, Set[int]], nodes: Set[int]): 
  return (len(topologicalSort(g, nodes)) == len(nodes))


#TODO - other variations of detect cycles