  # 133. Clone Graph
# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
 

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
      
      if not node: return None
    
      # 1. Just think about creating a dictionary of nodes first
      clone = {}

      def dfs(n):
        if n in clone: return clone[n] # clone serving as seen also
        cn = clone[n] = Node(n.val)
        
        for nb in n.neighbors:  ## Note: no seen, because we worry about all edges, not just seeing all nodes
          cnb = dfs(nb)  
          cn.neighbors.append(cnb) ## 2. Then worry about connections. 
          ## Important: Don't do both ways!! As you'll call dfs from cnb as well.  
            
        return cn
        
      dfs(node)
      return clone[node]
        