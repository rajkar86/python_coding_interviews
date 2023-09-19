# 224. Basic Calculator
# Implement a basic calculator to evaluate a simple expression string.

# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

# Example 1:

# Input: "1 + 1"
# Output: 2
# Example 2:

# Input: " 2-1 + 2 "
# Output: 3
# Example 3:

# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23
  

def calculate(s: str) -> int:
  
  res = 0
  curr = 0
  sign = 1 # prv sign
  flip = [1] # stack of signs before parantheses, every paranthesis is effectively like a potential flip of signs 

  for c in s:
    if c.isdigit():
      curr = 10*curr + int(c)
    elif c in "+-":
      res += curr * sign * flip[-1]
      curr = 0
      sign = 1 if c == "+" else -1
    elif c == '(':
      flip.append(sign*flip[-1])
      sign = 1
    elif c == ")": 
      res += curr * sign * flip.pop()
      curr, sign = 0, 1
              
  res += curr*sign* flip.pop()
  return res


def calc(s: str) -> int:
  res = 0
  curr = 0
  sign = 1 # prv sign
  for c in s:
    if c.isdigit(): 
      curr = 10*curr + int(c)
    elif c in "+-":
      res += curr*sign
      curr = 0
      sign = 1 if c == "+" else -1
              
  res += curr*sign
  return res


print(calc("-1-2+3-3+4"))
print(calculate("-(-1-1)+3"))