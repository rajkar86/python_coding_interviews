# Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
  
  
def removeKdigits(num, k):
  if (len(num) <= k):
    return '0'

  # Let's try to re-form the number but 
  # anytime we find a number smaller than the number we have in the highest position so far, we throw it away
  # and make a note that we have thrown that number 
  res = [num[0]]
  for n in num[1:]:
    while (k > 0 and len(res) > 0 and n < res[-1]): 
      res.pop()
      k = k - 1
    res.append(n)

  # If we didn't exhaust k, we have a strictly increasing stack, throw away the last numbers
  for i in range(min(k, len(res))):
    res.pop()
  
  ## Find the first non-zero index 0 in case the beginning is 0
  for i in range(len(res)):
    if res[i] != '0':
      break
  
  return(''.join(res[i:]))
  

num = "1234567890"
k = 9
print(removeKdigits(num, k))
