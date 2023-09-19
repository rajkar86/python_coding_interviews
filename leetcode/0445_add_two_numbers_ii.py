
# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

# Example:

# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
  
  
# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x, n=None):
    self.val = x
    self.next = n


def addTwoNumbers(l1, l2):
  def rev(l):
    prev = None
    curr = l
    while curr is not None:
      nxt = curr.next
      curr.next= prev
      prev = curr
      curr = nxt
    return(prev)    
      
    
  l1 = rev(l1)
  l2 = rev(l2)

  
  rem = 0
  
  res = None
  curr = None
  
  while l1 or l2:
    
    s = rem
    if l1:
      s += l1.val
      l1 = l1.next
    if l2:
      s += l2.val
      l2 = l2.next
    
    n = ListNode(s % 10)
    if (res): # Can probably use dummy to simplify this
      curr.next = n
      curr = curr.next
    else:
      res = n
      curr = n
      
    rem = 1 if s >= 10 else 0
    
    
  if rem:
    curr.next = ListNode(1)

  res = rev(res)
  return(res)

      
      
l2 = ListNode(4, ListNode(2,  ListNode(9)))
l1 = ListNode(9, ListNode(2))
#printLL(addTwoNumbers(l1, l2))
