# 38. Count and Say

# The count-and-say sequence is the sequence of integers with the first five terms as following:

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.

# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

# Note: Each term of the sequence of integers will be represented as a string.

class Solution:
  
    def __init__(self, max_n=30):
      self.cache = [1] * max_n # Just for LC efficiency
      for i in range(1, max_n):
        self.cache[i] = self.next_num(self.cache[i-1])
    
    # function that takes a number in the sequence and returns the next
    def next_num(self, num):
          s = str(num)
          n = len(s)
          
          count = 0
          ret = ""
          for i in range(n): # Better to use index in these cases
            count += 1
            
            if i==n-1 or s[i] != s[i+1]:
              ret += str(count) + s[i]
              count = 0
                          
          return int(ret)
            
    def countAndSay(self, n: int) -> str:
      # validate inputs
      return str(self.cache[n-1])