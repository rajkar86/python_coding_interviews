# 668. Nearly every one have used the Multiplication Table. But could you find out the k-th smallest number quickly from the multiplication table?

# Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to return the k-th smallest number in this table.

from heapq import heapify, heappush, heappop

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        if (n < m) : self.findKthNumber(n, m, k)
        
        l = [(i+1, i+1, 1) for i in range(m)]
        heapify(l)
        
        for _ in range(k-1):
          num, i, times = heappop(l)
          if (times+1 <= n): heappush(l, (i*(times+1), i, times+1))
        
        num, i, times = heappop(l)
        
        return num

# Similar to 378