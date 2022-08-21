from typing import List
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        output = 0
        for i in range(len(piles)//3,len(piles), 2) :
                output += piles[i]
        return output
       
obj = Solution()
n = int(input('Enter number of piles: '))
piles = list(map(int, input('Enter the piles: ').strip().split()[:n]))
print(obj.maxCoins(piles))
