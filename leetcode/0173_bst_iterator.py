#173. Binary Search Tree Iterator


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

  def __init__(self, root: TreeNode):
    self.g = self.__inorder(root)
    self.cur = None
    self.next() 

  def __inorder(self, n):
    if not n: return
    yield from self.__inorder(n.left)
    yield n.val
    yield from self.__inorder(n.right)
    
  def next(self) -> int:
    ret = self.cur
    try:
      self.cur = next(self.g)
    except StopIteration:
      self.cur = None
    return ret

  def hasNext(self) -> bool:
    return self.cur is not None

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()