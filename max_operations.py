def maxOperations(nums, k):
        checkFinished, resetNums, originalNumsLength=False,False, len(nums) 
        while len(nums)>0 and checkFinished!=True:
            resetNums=False
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i]+nums[j]==k:
                        nums.remove(nums[j])
                        nums.remove(nums[i])                      
                        resetNums = True
                        break
                if resetNums:
                    break
                if i==len(nums):
                    checkFinished=True
            if checkFinished:
                break
        print(nums)
        return  (originalNumsLength-len(nums))//2 
print(maxOperations([1,2,3,4], 6))