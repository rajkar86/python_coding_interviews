# 752. Open the Lock

# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

# The lock initially starts at '0000', a string representing the state of the 4 wheels.

# You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

# Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

# Example 1:
# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation:
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".
# E

from collections import deque

deadends = ["0201","0101","0102","1212","2002"]
target = "0002"
      
      
# print(list(neighbors('1219')))

def openLock(deadends, target):
  def neighbors(s):
    l = list(map(int, s))

    for i in range(len(l)):
      for d in [1,-1]:
        lc = l.copy()
        lc[i] = (lc[i] + d) % 10
        yield (''.join(map(str, lc)))

  visited = set(deadends)
  q = deque()
  q.append('0000')
  turns = 1

  while q:
    sz = len(q)
    for _ in range(sz): # empty nodes at this level
      s = q.popleft()
      for n in neighbors(s):
        if n not in visited:
          if n == target:
            return (turns)
          q.append(n)
          visited.add(n)
        
    turns += 1

  return -1


print(openLock(deadends, target))
