# Given a string S and a string T, 
# find the minimum window in S which will contain 
# all the characters in P in complexity O(n).

s = "ADOBECODEBANC"
p = "ABC"

from collections import defaultdict

def minWindow(s, t):
  if len(p) > len(s) or len(p)==0: return ("")

  count = defaultdict(int) # positive is excess, neg is requirement
  for char in p: count[char] -= 1
  to_match = len(p)

  left, res = 0, []

  for right, char in enumerate(s):
    
    # State update for increasing the interval 
    if char in count: 
      if count[char] < 0: to_match -= 1
      count[char] += 1 # Can go above 0, meaning we have excess

    # Once toMatch becomes 0, we don't have to track it
    if to_match > 0: continue 
    
    #  State update for decreasing the interval
    while left < right:
      if s[left] in count:
        if count[s[left]] == 0: break
        count[s[left]] -= 1
      left += 1

    if len(res) == 0 or (res[1] - res[0]) > (right-left):
      res = (left, right)

  return (s[res[0]:res[1]+1] if res else "")

if __name__ == "__main__":
  print(minWindow(s, p))

### "at most" sliding window 

def numberOfSubarrays(self, A, k):
    def atMost(k):
        res = i = 0
        for j in range(len(A)): # Iterate over outer index
            k -= A[j] % 2 
            while k < 0: # Validate condition is still false (really just finding next odd number)
                k += A[i] % 2
                i += 1
            res += j - i + 1 ## Tip: think if condition is always true, you can ignore the while loop, the while loop is there to make the condition true and update i accordingly
        return res

    return atMost(k) - atMost(k - 1)
