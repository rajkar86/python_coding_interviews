# 395. Longest Substring with At Least K Repeating Characters

# Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

# Example 1:

# Input:
# s = "aaabb", k = 3
# Output:
# 3

# The longest substring is "aaa", as 'a' is repeated 3 times.

# Solution: 
# If every character appears at least k times, the string is the answer. 
# If not, split by any character that's less frequent than k, and recursively call the same function


import re, collections

def longestSubstring(s, k):
  if len(s) < k: return 0

  counter = collections.Counter(s)
  delim = "".join([key for key, v in counter.items() if v < k])

  if len(delim) == 0: return len(s)

  return max(longestSubstring(ss,k) for ss in re.split("[" + delim + "]", s))


print(longestSubstring("adaabbabsasf", 3))
