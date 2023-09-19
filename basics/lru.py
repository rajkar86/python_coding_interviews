from collections import OrderedDict
class LRUEasy(OrderedDict):
  'Limit size, evicting the least recently looked-up key when full'

  def __init__(self, maxsize=128, *args, **kwds):
    self.maxsize = maxsize
    super().__init__(*args, **kwds)

  def __getitem__(self, key):
    value = super().__getitem__(key)
    self.move_to_end(key)
    return value

  def __setitem__(self, key, value):
    if key in self:
      self.move_to_end(key)
    super().__setitem__(key, value)
    if len(self) > self.maxsize:
        oldest = next(iter(self))
        del self[oldest]


from dataclasses import dataclass

@dataclass
class Node:
  key: int = None
  val: int = None
  prv: 'Node' = None
  nxt: 'Node' = None
  
class LRUCache:

    def __init__(self, capacity: int):
      assert(capacity > 0)
      self.d = {}
      self.cap = capacity
      self.head = Node()
      self.tail = Node()
      self.head.nxt = self.tail
      self.tail.prv = self.head
    
    def _push(self, n: Node):
      h = self.head
      tmp = h.nxt
      h.nxt = n
      tmp.prv = n
      n.prv = h
      n.nxt = tmp
      
    def _remove(self, n: Node):
      assert(n!=self.head and n!=self.tail) ## Don't call it with head or tail
      n.prv.nxt = n.nxt
      n.nxt.prv = n.prv
      n.prv = None
      n.nxt = None # TODO Check

    def get(self, key: int) -> int:
      if key not in self.d: return -1
      n = self.d[key]
      self._remove(n)
      self._push(n)
      return n.val

    def put(self, key: int, value: int) -> None:
      if key in self.d: 
        n = self.d[key] # Just this self._remove(self._pop(n.key))
        del self.d[n.key]
        self._remove(n)
      elif len(self.d) == self.cap:
        n = self.tail.prv
        self._remove(n)
        del self.d[n.key]
        
      n = Node(key, value)
      self.d[key] = n # Don't forget to update the dictionary
      self._push(n)

### See 0146_lru_cache for other variations