# 32. Generate paranthesis
# Given n pairs of parentheses, 
# write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
    
def generateParenthesis(n: int):
    
  def helper(seq: str, left: int, right: int):

    if len(seq) == 2*n:        
        print(seq)
        return

    if left < n:
        helper(seq + "(", left+1, right)

    if right < left:
        helper(seq + ")", left, right+1)

  helper("", 0, 0)
    
    
def generateParenthesisDP(n: int):
    
  ans = [['']]
    
  for m in range(1,n+1):
    
    res = []
    for j in range(m):
      res += [x + '(' + y + ')' for x in ans[j] for y in ans[m-j-1]]
      # Note: Doing both will only create duplicates
    
    ans.append(res)    
    
  print (ans[n])
    
if __name__ == "__main__":
  import timeit
  a = timeit.timeit('generateParenthesis(3)', globals=globals(), number=100)
  b = timeit.timeit('generateParenthesisDP(3)', globals=globals(), number=100)
  print(a, b)
