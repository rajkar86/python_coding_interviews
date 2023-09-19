# 93. Restore IP Addresses

# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

# Example:

# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
  
  
s = "25525511135"
# s = "010010"

def restoreIpAddresses(s):
  res = []
  
  def isValid(ss):
    if ss == "0": return True
    return (len(ss) > 0 and ss[0] != "0" and int(ss) < 256)

  def helper(s, l):
    if len(l) == 3:
      if isValid(s): res.append(".".join(l + [s]))
      return
    
    for i in range(1,4):
      if isValid(s[:i]): helper(s[i:], l + [s[:i]])

  helper(s, [])

  return(res)

print(restoreIpAddresses(s))
