from dataclasses import dataclass

@dataclass
class Node:
  key: str 
  val: int
  next: 'Node' = None


class HashTable():

  def __init__(self, size):
    self.size = size
    self.buckets = [None] * self.size

  def hashing(self, k):
    return hash(k) % self.size
    # TODO common hash functions
    
  def put(self, k, v):
    h = self.hashing(k)
    head = self.buckets[h]
    
    if not head:
      self.buckets[h] = Node(k,v)
      return

    while head: #simpler to do head.next here and take the assignment out of the loop
      if head.key == k:
        head.val = v 
        return
      if not head.next:
        head.next = Node(k,v)
      head = head.next
    

  def get(self, k):
    h = self.hashing(k)
    head = self.buckets[h]

    while head:
      if head.key == k: return head.val 
      head = head.next       
    return None

  def remove(self, k):
    h = self.hashing(k)
    head = self.buckets[h]

    if not head: return 

    if head.key == k:
      self.buckets[h] = head.next
      return
    
    while head.next:
      if head.next.key == k:
        head.next = head.next.next
      head = head.next 

if __name__ == "__main__":

  h = HashTable(19)

  h.put("a", 1)
  print(h.get("a"))

  h.put("a", 2)
  print(h.get("a"))

  h.put("b", 4)
  print(h.get("b"))

  h.remove("a")
  
  print(h.get("a"))
  print(h.get("b"))