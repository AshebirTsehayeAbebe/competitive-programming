def numIdenticalPairs(nums):
 output=0
 for i, item in enumerate(nums):
     for j in range(i+1, len(nums)):
         if item==nums[j]:
             output+=1
 return output
size = int(input('Enter size: '))
nums = list(map(int, input('Enter elements: ').strip().split()[:size]))
print(numIdenticalPairs(nums))