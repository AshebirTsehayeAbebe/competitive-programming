from typing import List
class Solution:
   def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxFrequency, sum, start, end=0,0,0,0

        for end in range(len(nums)):
            sum+=nums[end]        
            while (end -start+1)*nums[end]-sum>k:
                sum-=nums[start]
                start+=1
            maxFrequency=max(maxFrequency, end -start+1)
        return maxFrequency

obj = Solution()
n=int(input('Enter array size: '))
nums  = list(map(int,input('Enter elements: ').strip().split()[:5]))

k=int(input('Enter number of operations: '))
print(obj.maxFrequency(nums, k))
    