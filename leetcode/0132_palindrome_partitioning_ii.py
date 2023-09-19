# 132. Palindrome Partitioning II

# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s.

# Example:

# Input: "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
# A

s = "amomcb"

def minCut(s):   
  n = len(s)
  dp = [[1] * n for i in range(n)] 
  # if s[i:(j+1)] a palindrome

  for d in range(1,n):
    for i in range(n-d):
      j = i+d
      dp[i][j] = int(s[i] is s[j]) and dp[i+1][j-1]
  
  cut = list(range(n+1))

  for j in range(1,n): ## Ending at j
    for i in range(j+1): ## Check every possible i before
      if dp[i][j]:
        cut[j+1] = min(cut[j+1], cut[i]+1) # Any time dp_ij is a palindrome, check if we can minimize our current estimate using that shortcut

  return cut[-1]-1

print(minCut(s)) 
