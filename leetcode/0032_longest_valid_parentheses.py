# 32. Longest Valid Parentheses
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

s = ")()())"

def longestValidParentheses(s):
  stack = []

  matches = [-1] * len(s) ## position of matching bracket
  for i, c in enumerate(s):
    if c == "(":
      stack.append(i)
    elif stack:
      pos = stack.pop()
      matches[pos] = i
      matches[i] = pos

  maxRun = 0
  run = 0
  for m in matches:
    if m < 0:
      run = 0
      continue
    # In this case, all we care about is that there is a match
    run += 1
    maxRun = max(maxRun, run)

  return(maxRun)
  
  
print(longestValidParentheses(s))