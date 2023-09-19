# You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

from collections import defaultdict

class Solution:
    def change(self, amount: int, coins) -> int:
      
      dp = defaultdict(int)
      dp[0] = 1
      
      for c in coins: ## c and i loops can be reversed
        for i in range(1,amount+1):
          if i-c in dp:
            dp[i] += dp[i-c]
            

      return dp[amount]