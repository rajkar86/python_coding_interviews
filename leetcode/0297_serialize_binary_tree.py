# 297. Serialize and Deserialize Binary Tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
      l=[]
      def h(r):
        l.append(str(r.val) if r else "#")
        if r:
          h(r.left)
          h(r.right)
      h(root)
      return ",".join(l)

    def deserialize(self, data):
        l = iter(data.split(","))
        def h():          
          v = next(l)
          r = None
          if v != "#": 
            r = TreeNode(int(v))
            r.left = h()
            r.right = h()
          return r
          
        return h()
        
# NOTE: Basically, it's easier if we have the root node first
#    
# TODO try - inorder
# Sparsity: do we just condense stretches of # ?? Think about it

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))