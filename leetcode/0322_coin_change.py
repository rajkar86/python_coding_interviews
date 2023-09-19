# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# Example 1:

# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1

import math 

def coinChange(coins, amount):

  dp = [0] + [math.inf] * amount
  
  for c in coins: ## c and i loops can be reversed
    for i in range(1,amount+1):
      if i >= c:
        dp[i] = min(dp[i], 1 + dp[i-c])
  
  
  return -1 if math.isinf(dp[-1]) else dp[-1]
  

def coinChangeBackTrackingWithMemo(self, coins, amount: int) -> int:
  
  coins = sorted(coins, reverse = True)
  
  memo = {}
  
  def helper(a):
    
    if a in memo: return memo[a]
    if a < 0: return math.inf 
    if a == 0: return 0
    memo[a] = 1 + min(helper(a - c) for c in coins)
    return memo[a]
  
  res = helper(amount)
  return -1 if math.isinf(res) else res 
  
amount = 11
coins = [1, 2, 5]
print(coinChange(coins, amount))
