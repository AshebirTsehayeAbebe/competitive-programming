from typing import List
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        minimizedPairSum=0
        for i in range(len(nums)//2):
            minimizedPairSum=max(minimizedPairSum,nums[i]+nums[len(nums)-i-1])
        return minimizedPairSum
obj = Solution()
n=int(input('Enter array size'))
nums=list(map(int, input('Enter array elements').strip().split()[:n]))
print(obj.minPairSum(nums))