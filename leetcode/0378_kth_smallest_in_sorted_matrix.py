# 378. Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

from heapq import heapify, heappush, heappop
from typing import List 

class Solution:
  def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    m = len(matrix)
    n = len(matrix[0])

    if k < n: return matrix[0][k-1]
    if k < m: return matrix[k-1][0]

    v = [(v, 0, j) for j, v in enumerate(matrix[0])]
    heapify(v)

    for _ in range(k-1):
      _, i, j = heappop(v)
      if i+1 < m: heappush(v, (matrix[i+1][j],i+1,j))

    return heappop(v)[0]
      