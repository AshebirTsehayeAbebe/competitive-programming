from inspect import _void


class Solution:
 def dominoPiling(self, m,n)->_void:
  print(m*n//2)
 
obj = Solution()
n = int(input("Enter your value: "))
m = int(input("Enter your value: "))
obj.dominoPiling(m,n)
    