# 1161. Maximum Level Sum of a Binary Tree

# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

import math

def maxLevelSum(root: TreeNode) -> int:
  max_sum = -math.inf
  max_ht = None
  ht = 1

  level = [root]
  while level:
    s = sum(n.val for n in level)
    if s > max_sum:
      max_ht = ht
      max_sum = s
    level = [c for n in level for c in [n.left,n.right] if c]
    ht += 1
  return (max_ht)