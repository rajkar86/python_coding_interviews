# 43. Multiply Strings
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"
  
from collections import defaultdict

def multiply(num1: str, num2: str) -> str:
      
    products = defaultdict(int)

    for i, x in enumerate(num1[::-1]):
      for j, y in enumerate(num2[::-1]):
        products[i+j] += int(x) * int(y)

    ret = ""
    carry = 0
    for i in range(len(num1)+len(num2)-1):
      s = products[i] + carry
      ret = str(s%10) + ret
      carry = s//10
      
    if carry:
      ret = str(carry) + ret
    
    return ret if int(ret) > 0 else "0"
  
  
print(multiply("328", "99"))