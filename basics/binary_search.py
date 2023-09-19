
def bisect_left(a, x, lo, hi): # When multiple matches are possible
    while lo < hi:
        mid = (lo+hi)//2 # don't forget integer division
        if a[mid] < x: lo = mid+1 # Use __lt__ to match the logic in list.sort() and in heapq
        else: hi = mid
        #if a[mid] > x: hi = mid # For bisect_right, or just use <= instead of < above
        #else: lo = mid+1
    return lo ## Be careful return lo, not mid

def binary_search(nums, target):
  
  # 1 Check
  if not nums[0] <= target <= nums[-1]: return 0

  l, r = 0, len(nums)-1
  while l <= r: # 2 <= NOT < 
    m = l + (r-l)//2
    val = nums[m]
    if val == target: 
      return m
    if val < target:
      l = m+1 #3 m+1 NOT m
    else:
      r = m-1 #4 m-1 NOT m
  
  return -1
      
print(binary_search([1,2,3,4,5,6], 4))
print(binary_search([1,2,3,5,6], 4))


def search(nums, target):
  
  n = len(nums)
  
  m = 0
  if nums[0] > nums[-1]:
    ## Binary search # 1 - conditions are different
    l, r = 0, n-1
    while l <= r:
      m = l + (r-l)//2
      if nums[m] < nums[m-1]: break #1 break - condition
      if nums[m] < nums[0]:  #2 split - condition
        r = m
      else:
        l = m+1
  idx = m
  
  f = lambda x: (x+idx)%n
  
  ## Binary search 2 - but tranform index whenever you access the array
  if not nums[f(0)] <= target <= nums[f(n-1)]: return -1

  l, r = 0, n-1
  while l <= r:
    m = l + (r-l)//2
    i = f(m)
    val = nums[i]
    if val == target:
      return i
    if val < target:
      l = m+1
    else: 
      r = m-1
  
  return -1

print(search([4,5,6,7,0,1,2], 1))
print(search(range(1, 10), 4))