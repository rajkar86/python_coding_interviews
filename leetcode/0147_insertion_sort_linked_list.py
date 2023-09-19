# 147. Insertion Sort List

# Sort a linked list using insertion sort.
# Algorithm of Insertion Sort:

# Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
# It repeats until no input elements remain.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        
        if not head or not head.next: return head
        
        def insert(node):
          s = dummy
          while s.next.val < node.val: s = s.next
          s.next, node.next = node, s.next
          
        prev = head
        while prev and prev.next:
          if prev.val <= prev.next.val: 
            prev = prev.next
            continue
          nxtNode = prev.next.next
          insert(prev.next)
          prev.next = nxtNode
          
        return dummy.next
