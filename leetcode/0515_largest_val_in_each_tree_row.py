515. Find Largest Value in Each Tree Row

# You need to find the largest value in each row of a binary tree.

# Example:
# Input: 

#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 

# Output: [1, 3, 9]

# Easier to do level order traversal
class T(object):
  def __init__(self, x, l=None, r=None):
    self.val = x
    self.left = l
    self.right = r
    
def largestValues(root):
  res = []

  def helper(n, level):
    if level == len(res):
      res.append(n.val)
    else:
      res[level] = max(res[level], n.val)

    if n.left:
      helper(n.left, level+1)
    if n.right:
      helper(n.right, level+1)

  if root:
    helper(root, 0)
  return res
  

root = T(1,T(3, T(5),T(3)),T(2,None,T(9)))

print(largestValues(root))
