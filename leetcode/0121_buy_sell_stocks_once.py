# 121. Best Time to Buy and Sell Stock
# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

import math
from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    minp = math.inf
    ret = 0
    for p in prices:
      minp = min(p, minp)
      ret = max(ret, p-minp) 
    return ret
