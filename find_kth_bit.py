class Solution:
    def solve(self,s):
        t=[]
        for ch in s:
            if(ch=='1'):
                t.append('0')
            else:
                t.append('1')
        t.reverse()
        s=s+'1'+''.join(t)
        return s
    def findKthBit(self, n: int, k: int) -> str:
        s='0'
        for i in range(n):
            s=self.solve(s)
        return s[k-1]
