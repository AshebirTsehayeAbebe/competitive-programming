class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left=ans=oddCount=count=0
        for right in range(len(nums)):
            if nums[right]%2==1:
                oddCount+=1
                count=0
            while oddCount==k:
                if nums[left]%2==1:
                    oddCount-=1
                left+=1
                count+=1
            ans+=count
        return ans
