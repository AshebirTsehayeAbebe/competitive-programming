class Solution:
    def countGoodNumbers(self, n: int) -> int:
        result, x, i=5**(n%2), 20, n//2
        while i>0:
            if i%2==1:
                result=result*x%(10**9+7)
            x=x*x%(10**9+7)
            i//=2
        return result
