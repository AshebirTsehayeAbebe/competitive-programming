from collections import Counter
from typing import List
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        count=1
        output=0
        for item in counts.most_common():
            output+=item[1]
            if output >=len(arr)//2:
                break
            count+=1
        return count
obj= Solution()
n=int(input('Enter array size: '))
arr=list(map(int,input('Enter array elements: ').strip().split()[:n]))
print(obj.minSetSize(arr))
