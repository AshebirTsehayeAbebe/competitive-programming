from typing import List
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        maximumCoins=0
        piles.sort()
        while len(piles)>0:            
            maximumCoins+=piles[len(piles)-2]
            piles.remove(piles[len(piles)-2])
            piles.remove(piles[len(piles)-1])
            piles.remove(piles[0])            
        return maximumCoins
       
obj = Solution()
n = int(input('Enter number of piles: '))
piles = list(map(int, input('Enter the piles: ').strip().split()[:n]))
print(obj.maxCoins(piles))

"""
Time Complexity:
worst case- n log n
best case- n log n
"""