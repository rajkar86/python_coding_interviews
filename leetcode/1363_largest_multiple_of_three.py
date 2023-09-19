# 1363. Largest Multiple of Three

# Given an integer array of digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order.

# Since the answer may not fit in an integer data type, return the answer as a string.

# If there is no answer return an empty string.

 

# Example 1:

# Input: digits = [8,1,9]
# Output: "981"
# Example 2:

# Input: digits = [8,6,7,1,0]
# Output: "8760"

digits = [8,6,7,1,0]
# digits = [0,0,0,0,0,0]

def largestMultipleOfThree(digits):
  digits.sort()
  rem = [d % 3 for d in digits]
  s = sum(rem) % 3
  if s != 0:
    try:
      del digits[rem.index(s)]
    except ValueError:
      del digits[rem.index(3-s)]
      del digits[rem.index(3-s)]

  if len(digits) == 0: return ""
  if digits[-1] == 0: return "0"
  return ("".join(str(d) for d in reversed(digits)))


print(largestMultipleOfThree(digits))
