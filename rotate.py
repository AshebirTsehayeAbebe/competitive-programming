class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
            counter=0
            while counter<k:
                temp=nums.pop()
                nums.insert(0,temp)
                nums[0]=temp
                counter+=1
