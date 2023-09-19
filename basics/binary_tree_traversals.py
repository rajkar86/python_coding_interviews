# Binary tree traversals

from collections import deque
class TreeNode:
    def __init__(self, data, left=None, right=None):
      self.left = left
      self.right = right
      self.data = data
        
    def inorder(self):
      res = []
      if (self.left): res = res + self.left.inorder()
      res.append(self.data)
      if (self.right): res = res + self.right.inorder()
      return res

    def levelOrder1(self):
      if not self: return []
      res, level = [], [self]
      while level:
        res.append([x.data for x in level])
        level = [c for n in level for c in [n.left, n.right] if c]
      return res
    
    def levelOrder(self):
      res, nodes = [], []
      curr, prev = deque(), deque()
      prev.append(self)
      
      while prev:
        n = prev.popleft()
        nodes.append(n.data)
        if (n.left): curr.append(n.left)
        if (n.right): curr.append(n.right)
        if not prev:
          prev=curr
          curr=deque()
          res.append(nodes)
          nodes=[]
      return res
    
    ### Iterative in order
    def inOrderTraversalIter(self):
      root = self
      if not root: return []
      res, stack = [], []
      curr = root
      
      while curr or stack: 
        while curr: # Keep going left until you can't
          stack.append(curr)
          curr = curr.left
        if stack: # add the value of left node to res, and go right
          n = stack.pop() 
          res.append(n.val)
          curr = n.right 

      ### Iterative preorder is simple. Print, add right node and left node to stack
      ### Iterative post-order is reverse-pre-order of mirror tree.

    
root=TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None,TreeNode(4)))
print(root.inorder())
print(root.levelOrder())
print(root.levelOrder1())


## Morris traversal
def morris__inorder_traversal(root): 

  current = root 
    
  while current is not None: 
        
      if current.left is None: 
          yield current.data 
          current = current.right 
      else: 
          # Find the inorder predecessor of current 
          # But check that it's not current (because we added it before)
          # Before taking care of the left sub-tree, it'll stop because of the first condition
          # After taking care of the left sub-tree, it'll stop because of the second condition
          pre = current.left 
          while (pre.right is not None) and (pre.right is not current): 
              pre = pre.right 

          if pre.right is None: 
              # Make current as right child of its inorder predecessor 
              pre.right = current     # adding to find the way back once left tree is done
              current = current.left  

          else: # pre.right is current
              # Revert the changes made in the 'if' part
              pre.right = None
              yield current.data 
              current = current.right 