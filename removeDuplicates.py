class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic={}
        for i in range(len(nums)):
            if dic.get(nums[i]):
                nums[i]="_"
            else:
                dic[nums[i]]=True
        i=0
        for item in dic:
            nums[i]=item
            i+=1
        return len(dic)
