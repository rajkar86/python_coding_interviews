from collections import defaultdict, Counter
import math

def minCoins(coins, amount):
    
  memo = {}
  
  # Instead, we could just use @cache (from functools import cache)
  def helper(a):
    
    if a in memo: return memo[a]
    if a < 0: return math.inf 
    if a == 0: return 0
    memo[a] = 1 + min(helper(a - c) for c in coins)
    return memo[a]
  
  res = helper(amount)
  return -1 if math.isinf(res) else res 
  
from functools import lru_cache


# Prefer no return version below 
def listCombinationsReturn(amount, coins):

  @lru_cache(maxsize=None)  # or @cache
  def helper(a, start):
    
    if a < 0: return []
    if a == 0: return [[]]
    
    ret = []
    for i in range(start, len(coins)):   
      c = coins[i]
      ret += [[c] + l for l in helper(a-c, i)] 
      # won't treat different orderings as unique because if we add a later number then we can only add that number or ones after (canonical ordering)
      # change i -> i+1 if there's no reuse 
    
    return ret
  
  return  helper(amount, 0)


def listCombinations(amount, coins):        
      
      ret = []
      
      def helper(a, start, path):
        
        if a < 0: return
        
        if a == 0:
          ret.append(path)
          return
        
        for i in range(start, len(coins)):
          c = coins[i]
          helper(a-c, i, path + [c])
      
      helper(amount, 0, [])
      return ret


def listCombinationsDup(amount, coins):        

      ret = []
      coins.sort() ## For dup handling
      
      def helper(a, start, path):
        
        if a < 0: return
        
        if a == 0:
          ret.append(path)
          return
        
        for i in range(start, len(coins)):
          if i > start and coins[i] == coins[i-1]: continue # For dup handling, beware: continue
          c = coins[i]
          helper(a-c, i + 1, path + [c]) ## j+1 because of no-reuse
      
      helper(amount, 0, [])
      return ret
