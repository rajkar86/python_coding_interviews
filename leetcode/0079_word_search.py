# 79. Word Search

# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Solution:
# DFS with different handling of seen

from typing import List

def exist(board: List[List[str]], word: str) -> bool:
  if not board: return False
  
  r, c = len(board), len(board[0])
  N = len(word)
  
  def dfs(n, start = 0, seen = None):
    x, y = n[0], n[1]
    
    if not 0 <= x < r or not 0 <= y < c:  return False # Out of range
    
    if seen is None: seen = set()
    if n in seen: return False
    
    if board[x][y] != word[start]: return False # No match
    if start == N-1: return True ## Success
    
    seen.add(n) ## Add only if there's a match
    ret = any(dfs(nb, start+1, seen) 
              for nb in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)])
    
    seen.remove(n) ## Remove if we can't complete
    return ret
  
  
  return any(dfs((i,j)) for i in range(r) for j in range(c))
  
  
board = [["a","b"]]
word = "ba"

board = [
  ['A','B','C','E'],
  ['S','F','E','S'],
  ['A','D','E','E']
]

word = "ABCCED"
word="ABCESEEEFS"



print(exist(board, word))