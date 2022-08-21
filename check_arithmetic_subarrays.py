from typing import List
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for index in range(len(l)):
            temArray=nums[l[index]:r[index]+1]
            if len(temArray)<2:
                answer.append(False)
                break
                
            temArray.sort()
            difference = temArray[1]-temArray[0]
            isArithmetic =True
            
            for i in range(2, len(temArray)):
                if temArray[i]-temArray[i-1]!=difference:
                    isArithmetic=False
                    break
            answer.append(isArithmetic)
            
        return answer
obj = Solution()

n = int(input('Enter size of the array: '))
nums = list(map(int, input('Enter array elements: ').strip().split()[:n]))

m = int(input('Enter size of range queries: '))
l = list(map(int, input('Enter first range query: ').strip().split()[:m]))
r = list(map(int, input('Enter second range query: ').strip().split()[:m]))
print(obj.checkArithmeticSubarrays(nums, l, r))



"""
Time complexity:
Worst case- n^2(logn)
Best case- n
"""