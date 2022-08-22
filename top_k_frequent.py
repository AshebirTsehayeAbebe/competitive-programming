from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        output=[]
        for item in counts.most_common(k):
            output.append(item[0])
        return output
obj= Solution()
n=int(input('Enter array size: '))
arr=list(map(int,input('Enter array elements: ').strip().split()[:n]))
print(obj.minSetSize(arr))