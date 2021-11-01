import math
class Solution:
   def solve(self, n):
      return math.factorial(n)
ob = Solution()
print(ob.solve(3))


import math

def solution(n, k):
    x = (n//k)**2
    f=math.factorial(k)

    return x*f