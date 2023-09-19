class DSU():
  def __init__(self, n):
    self.id = list(range(n))
    self.rank = [0] * n
    # Ranks are used instead of height or depth because path compression will change the trees’ heights over time.

  def find(self, x):
    if self.id[x] != x:
        self.id[x] = self.find(self.id[x])  # Path compression
    return self.id[x]
    ## TODO try using base-case

  def union(self, x, y):
    cx, cy = self.find(x), self.find(y)
    rx, ry = self.rank[cx], self.rank[cy]
    
    if cx == cy: return (False)      # Already connected
    if rx < ry: cx, cy = cy, cx      # Make y smaller rank
    self.id[cy] = cx                 # *** Important NOT self.id[y] = x ***
    if rx == ry: self.rank[cx] += 1  # Update rank if the ranks are same

    return (True)

    