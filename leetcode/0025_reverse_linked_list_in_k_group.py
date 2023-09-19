# 25. Reverse Nodes in k-Group
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# Example:

# Given this linked list: 1->2->3->4->5

# For k = 2, you should return: 2->1->4->3->5

# For k = 3, you should return: 3->2->1->4->5

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

    def reverse(h):
      p, c = None, h
      while c:
        tmp = c.next
        c.next = p
        p = c
        c = tmp 
      return p, h # rev_head, rev_tail


    dummy = ListNode(0, head)
    ptr_to_part_head = dummy

    while True:
      curr = ptr_to_part_head
      for _ in range(k):
        if not curr.next: return dummy.next
        curr = curr.next

      # Cut at the next tail
      tmp = curr.next
      curr.next = None

      # Reverse this part until the cut tail
      h, t = reverse(ptr_to_part_head.next)
      print(h, t)
      
      ## Attach the head and tail of reversed parts
      ptr_to_part_head.next = h
      t.next = tmp
      ptr_to_part_head = t          
        
      
      
        