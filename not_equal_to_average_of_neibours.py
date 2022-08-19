from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        mid = (len(nums)-1)//2
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]
        return nums
obj = Solution()
n = int(input('Enter size: ').strip())
nums = list(map(int, input('Enter elements: ').strip().split()[:n]))
print(obj.rearrangeArray(nums))
