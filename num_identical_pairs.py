from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        output=0
        for i, item in enumerate(nums):
            for j in range(i+1, len(nums)):
                if item==nums[j]:
                    output+=1
        return output
obj = Solution()
size = int(input('Enter size: '))
nums = list(map(int, input('Enter elements: ').strip().split()[:size]))
print(obj.numIdenticalPairs([1,2,3]))