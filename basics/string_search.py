

# Worst case is o(nm) to find ALL alignments, if there's no match or to find one match, it's o(n+m) -CHECK
# But average case is usually better o(n/m)
def boyer_moore(string, pattern):
  
  # This can be a list of 256 if you have ASCII characters TODO check 
  lastIndex = {s: i for i, s in enumerate(pattern)}

  n, m = len(string), len(pattern)
  
  if m == 0 or n < m: return -1

  i = 0
  while i < n-m:

    j = m-1 # Loop until you don't match. Do NOT have to check anything in the inner loop
    while j >= 0 and string[i+j] == pattern[j]:
      j -= 1 
    
    if j < 0: return i # Success

    # Jump smartly [either 1 (normal) or if last index of current char in string is behind j]
    li = lastIndex.get(string[i+j], -1)  # Confirm that -1 is default val? TODO
    i += j - li if li < j else 1 # max(j-li, 1) ? TODO
    
  return -1

# KMP: case where the table building stage uses the same idea as the string search
# table building stage - think of it as same case but the pattern is the string
#       
# A B A B C A B A B A B  [Pattern]
# 0 0 1 2 0 1 2 3 4 
#         p         i
# A B A B C A B A B A B  [String = pattern]
# We know (p-1) matched with (i-1) and we fail at the next step
# If

# worst case is O(m + n), m preprocess, 2 n comparisons
# See expanded version below
def kmp_gen(string, pattern):
  
  m = len(pattern)
  skip = [0] * m ## skip (longest proper prefix which is also suffix)

  def helper(pat, text, start=0):
    i, p = start, 0
    while i < len(text):

      if text[i] == pat[p]: 
        yield i, p+1
        p += 1
        i += 1
        continue 
      
      # No match
      if p == 0: 
        i += 1
      else: 
        p = skip[p-1] ### Basically, we were greedy, now we're testing if there's a shorter pattern that'll work. 

  for i, l in helper(pattern, pattern, 1): 
    skip[i] = l
  
  for i, l in helper(pattern, string): 
    if l == m: return (i - m + 1)

  return -1


def kmp(string, pattern):
  
  n, m = len(string), len(pattern)

  skip = [0] * len(pattern) ## skip (longest proper prefix which is also suffix)
  p = 0
  i = 1 # skip[0] is always 0; otherwise infinite loop can happen when skip is 1 at both 0 and 1
  while i < m:

    if pattern[i] == pattern[p]: 
      skip[i] = p + 1
      p += 1
      i += 1
      continue # Note
    
    # No match
    if p > 0:
      p = skip[p-1] # Case illustrated above
    else:
      i += 1

  p = 0
  i = 0  ### Difference 1
  while i < n:
    if string[i] == pattern[p]: ## Difference 2
      if p == m-1: return (i - m + 1) ### Difference 3
      i += 1
      p += 1
      continue
    
    # No match
    if p > 0:
      p = skip[p-1] # Case illustrated above
    else:
      i += 1

  return -1





if __name__ == "__main__":
  
  string = "hello" 
  pattern = "ll"

  print (boyer_moore(string, pattern))
  print (boyer_moore(string, pattern))