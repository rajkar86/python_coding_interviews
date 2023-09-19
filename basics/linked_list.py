# Linked lists
class Node:
    def __init__(self, data, nextN=None):
        self.data = data
        self.next = nextN

''' Alternative
from dataclasses import dataclass

@dataclass
class Node:
  val: int
  nxt: 'Node' = None
'''

def reverseListRec(head):
    if not head or not head.next.next: return head
    rest = reverseListRec(head.next)
    head.next.next = head
    head.next = None
    return rest

def reverseList(head):
  prev = None
  curr = head
  while curr:
      n = curr.next 
      curr.next = prev
      prev = curr
      curr = n
  return prev

def mergeTwoSortedLists(l1, l2):
    dummy = curr = Node(None)
    while l1 and l2:
        if l1.val > l2.val: l1, l2 = l2, l1 
        curr.nxt = l1
        curr = curr.nxt
        l1 = l1.next
    curr.nxt = l1 or l2
    return dummy.next

def mergeKLists(lists):
    n = len(lists)
    if n == 0: return None
    while n > 1:
        for i in range(n//2):
            lists[i] = mergeTwoSortedLists(lists[i], lists.pop())
        n = len(lists)
    
    return lists[0]

def isPalindrome(self, head):
    fast = slow = head
    # find the mid node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # slow is at mid for odd, right of middle two when even

    # reverse the second half
    mid = reverseList(slow)
   
    # compare the first and second half nodes
    while mid: # while prev and head:
        if mid.val != head.val:
            return False
        mid = mid.next
        head = head.next
    return True

    
class LinkedList:
    def __init__(self, head):
        self.head = head
    
    @classmethod
    def from_array(cls, a):
        v = list(map(lambda x: Node(x), a))
        v.append(None)
        for i in range(len(v)-1):
            v[i].next = v[i+1]
        return (cls(v[0]))
    
    def insertFirst(self, val):
        self.head=Node(val, self.head)
        
    def insertLast(self, val):
        n = self.head 
        while n.next is not None:
            n=n.next
        n.next=Node(val)
        
    def insertAfterNode(self, node: Node, val: int):
        node.next = Node(val, node.next)
         
    def print(self):
        n = self.head
        while n is not None:
            print(n.data, end=" ")
            n=n.next
        print("")

a=LinkedList.from_array(range(4))
a.print()
a.insertAfterNode(a.head.next.next, 2.5)
a.insertFirst(-1)
a.insertLast(4)
a.print()

#list is Stack
#“from collections import deque”
#deque append and pop - Stack
#deque append and popLeft - Queue
#deque appendLeft and pop - Queue
