# 1138. Alphabet Board Path
# On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

# Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.

class Solution:
  pos = {chr(i+ord('a')):(i//5, i%5) for i in range(26)}
  
  def alphabetBoardPath(self, target: str) -> str:
    
    def travel(a, b):
      r1, c1 = Solution.pos[a]
      r2, c2 = Solution.pos[b]
      ret = ""
      if c1 > c2: ret += "L"*abs(c1-c2)
      if r1 > r2: ret += "U"*abs(r1-r2)
      if c1 < c2: ret += "R"*abs(c1-c2)
      if r1 < r2: ret += "D"*abs(r1-r2)
      ret += "!"
      return ret
    
    ret = ""
    prv = 'a'
    for c in target:
      ret += travel(prv, c)
      prv = c
      
    return (ret)