class BinHeap:
  def __init__(self):
    self.heap = []
    
  def parent(self, i):
    p = (i-1)//2
    return p if p >= 0 else None
  
  def minChild(self,i):
    n = len(self.heap)
    if n < 2*i+2: return None # no child
    if n == 2*i+2: return 2*i+1 # One child
    return 2*i+1 if self.heap[2*i+1] < self.heap[2*i+2] else 2*i+2

  def swap(self, i, j):
    x = self.heap
    x[i], x[j] = x[j], x[i]
    
    
  def siftUp(self,i):
    p = self.parent(i)
    while p is not None and self.heap[i] < self.heap[p]:
      self.swap(i,p)
      i,p=p,self.parent(p)

  def insert(self,k):
    self.heap.append(k)
    self.siftUp(len(self.heap)-1)

  def siftDown(self,i):
    c = self.minChild(i)
    while c is not None and self.heap[i] > self.heap[c]:
      self.swap(i,c)
      i,c=c,self.minChild(c)

  # remove element at position i
  def pop(self, i=0):
    if not self.heap: return None
    retval = self.heap[i]
    self.heap[i] = self.heap[-1]
    self.heap.pop()
    self.siftDown(i)
    return retval

  def buildHeap(self,nums):
    self.heap =  nums[:]
    p = len(nums)//2 # largest parent with a child in range
    for i in reversed(range(p)):
      self.siftDown(i)

bh = BinHeap()

bh.buildHeap([9,5,6,2,3])
bh.insert(4)
print(bh.heap)

print(bh.pop())
print(bh.pop())
print(bh.pop())
print(bh.pop())
print(bh.pop())
