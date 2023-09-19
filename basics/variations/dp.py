

from collections import defaultdict, Counter
import math

def minCoinsDp(coins, amount): # See 322 for backtracking

  dp = [0] + [math.inf] * amount
  
  for c in coins: # c and i loops can be reversed (permutation)
    for i in range(1,amount+1): # optimize the loop, range(c,) and don't need to check before
      if i >= c:
        dp[i] = min(dp[i], 1 + dp[i-c])
  
  return -1 if math.isinf(dp[-1]) else dp[-1]

def numCombinationsDp(amount, coins):

  dp = defaultdict(int)
  dp[0] = 1
  
  for c in coins: ## loop over c first, cannot be reversed
    for i in range(1,amount+1): # Reverse for no reuse 
      if i-c in dp:
        dp[i] += dp[i-c]
        
  return dp[amount]

def listCombinationsDp(amount, coins):

  dp = defaultdict(list)
  dp[0] = [[]]

  for c in coins:
    for i in range(1,amount+1):
      if i-c in dp:
        for l in dp[i-c]: ## One more loop to loop over the combinations, or use dp[i] += [[c] + l for l in dp[i-c]]
          dp[i].append([c] + l) 

  return dp[amount]

def listCombinationsDupDp(amount, coins): # Dup, no re-use of course

  dp = defaultdict(list)
  dp[0] =[[]] 
  
  for c, count in Counter(coins).items():
    ret = defaultdict(list)   ## Tmp dict *before* looping over times
    for times in range(1,count+1):   
      n = c * times  
      curr = [c] * times
      for i in reversed(range(amount+1)):
        if i-n in dp:
          ret[i] += [curr + d for d in dp[i-n]]
          
    for k in set(dp) | set(ret): dp[k] += ret[k]

  return dp[amount]
