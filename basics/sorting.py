### Sorting 

## Mergesort (Divide and conquer)
# Useful for counting inversions (count smaller elements after each position)

from heapq import merge

def mergeSort(a): 
  
  ### If you can't use heapq merge
  # def merge_(L, R):
  #   n = len(L) + len(R)
  #   res = [0] * n
  #   for i in reversed(range(n)):
  #     if L and R:
  #       t = L if L[-1] > R[-1] else R  # perfectly fine in python as long as else case is also handled
  #     else:                            # If you don't define here, will raise NameError
  #       t = L if L else R
  #     res[i] = t.pop()
  #   return res
  
  if len(a) <= 1: return a
  mid = len(a) // 2
  L, R = mergeSort(a[:mid]), mergeSort(a[mid:])
  # Any sort of inversion count can happen here or inside merge
  return list(merge(L,R)) # or merge_(L,R)

## Heapsort

import heapq
def heapsort(nums):
  heapq.heapify(nums)
  return [heapq.heappop(nums) for i in range(len(nums))]

# Quicksort
# Can choose pivot to be random, or middle, or median of hi, lo and mid
# o(n^2) worst case if pivot is always the max or min
def quicksort(arr):
  
  def partition(lo, hi):
    pivot = arr[lo] # fix first element as pivot
    p = lo # index after which to accumulate elements >= pivot
    
    for i in range(lo+1, hi): 
      if arr[i] <= pivot:
        p += 1
        arr[i], arr[p] = arr[p], arr[i]
    
    # Handle the pivot at the end
    arr[p], arr[lo] = arr[lo], arr[p]
    return p # check!!!!
  
  ### Unused - replaced by TCO version below
  def sort1(lo, hi):
    if lo < hi: # Don't forget this <, not <= unlike binary search 
      p = partition(lo, hi)
      sort1(lo, p) # Don't include pivot in either call 
      sort1(p+1, hi)
  
  ## Tail call optimization TCO version
  def sort2(lo, hi):
    while lo < hi:  ### 1. if -> while
      p = partition(lo, hi)
      sort2(lo, p)
      lo = p + 1    ### 2. change line
  
  ## TCO w/ always choosing the smaller partition
  ## Unless you do this, recursion depth cannot be guaranteed
  def sort(lo, hi):
    while lo < hi:  
      p = partition(lo, hi)
      if p-lo < hi-p-1: ### 3. Choose the smaller partition 
        sort(lo, p)
        lo = p+1        ### 4. Update either lo or hi for the other call
      else:
        sort(p+1, hi)
        hi = p
      

def countingSort(nums):
  lo, hi = min(nums), max(nums)
  count = [0] * (hi - lo + 1)
  
  for n in nums:
    count[n-lo] += 1
  
  for i in range(1,len(count)):
    count[i] += count[i-1]
  
  out = [0] * len(nums)
  for n in reversed(nums): # reversed only important for stable sort when you extend to radix
    count[n-lo] -= 1
    out[count[n-lo]] = n
  
  return out

## TODO: radix sort 


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

# O(N^2)
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
