from array import array
import math
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        output=[]
        for i in range(1, len(points)):
            j=i-1
            key=points[i]
            keyDistance = math.sqrt(key[0]*key[0]+key[1]*key[1])
            currentItemDistance = math.sqrt(points[j][0]*points[j][0]+points[j][1]*points[j][1])
            while(j>=0 and keyDistance < currentItemDistance):
                points[j+1]=points[j]
                j-=1
                currentItemDistance = math.sqrt(points[j][0]*points[j][0]+points[j][1]*points[j][1])
            points[j+1]=key
        for i in range(k):
            output.append(points[i])
            
        return output
obj = Solution()
points= [[3,3],[5,-1],[-2,4]]
k=int(input('Enter value of k: '))
print(obj.kClosest(points, k))
