# 146. LRU Cache

from dataclasses import dataclass

@dataclass
class Node:
  key: int = None
  val: int = None
  nxt: 'Node' = None
  
class LRUCache:

    def __init__(self, capacity: int):
      assert(capacity > 0)
      self.prev_dict = {}
      self.cap = capacity
      self.head = Node()
      self.tail = self.head # Tail has latest node
      
    def _remove_next(self, prev):
      old = prev.nxt
      prev.nxt = old.nxt
      if old.nxt: 
        self.prev_dict[old.nxt.key] = prev
      else:
        self.tail = prev
      self.prev_dict[old.key] = None
      del self.prev_dict[old.key]
      del old

    def _addToTail(self, n):
      self.tail.nxt = n
      self.prev_dict[n.key] = self.tail 
      self.tail = n      

    def get(self, key: int) -> int:
      if key not in self.prev_dict: return -1 
      prev = self.prev_dict[key]
      n = prev.nxt
      if n != self.tail: # Be careful to handle this case
        self._remove_next(prev)
        self._addToTail(n)
      return n.val

    def put(self, key: int, value: int) -> None:
      if key in self.prev_dict:
        prev = self.prev_dict[key]
        if prev.nxt == self.tail: 
          prev.nxt.val = value
          return
        self._remove_next(prev)
      elif len(self.prev_dict) == self.cap:
        self._remove_next(self.head)
        
      self._addToTail(Node(key, value))


# TODO - # Head has latest node version 
# If we want the n latest items with n < Capacity, head being the latest is better